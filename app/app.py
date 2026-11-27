
import os
import gradio as gr

from phase10.app.aws_endpoint import ask_sagemaker
from phase10.app.safety import (
    needs_plan_details,
    plan_details_response,
)

BACKEND = os.getenv("INFERENCE_BACKEND", "local").lower()

SYSTEM_PROMPT = (
    "You are a US Health Insurance Educational Assistant. "
    "Explain US health insurance concepts accurately in simple English. "
    "Do not invent insurance rules, coverage details, premiums, or costs. "
    "Never assume the user has Medicare, Medicaid, or any specific insurance plan "
    "unless the user explicitly mentions it. "
    "Clearly distinguish general health insurance information from plan-specific information. "
    "If a question depends on the user's insurance plan, explain that the answer "
    "cannot be confirmed without the relevant plan details. "
    "For exact premiums, deductibles, copayments, coinsurance, or coverage, "
    "do not guess or provide unsupported amounts. Ask for the necessary details "
    "when appropriate. "
    "If you are uncertain, clearly acknowledge the uncertainty instead of guessing. "
    "Show calculation steps when answering numerical insurance questions. "
    "Provide educational information only. "
    "Do not make official coverage or eligibility decisions."
)

model = None
tokenizer = None


def load_local_model():
    global model, tokenizer

    import torch
    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        BitsAndBytesConfig,
    )

    model_path = "phase10/model/merged_best_epoch1"

    print("Loading local tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    print("Loading local model in 4-bit...")
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        quantization_config=quantization_config,
        device_map="auto",
        low_cpu_mem_usage=True,
    )

    model.eval()
    print("Local fine-tuned model loaded successfully.")


def respond_local(question):
    import torch

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = {
        key: value.to(model.device)
        for key, value in inputs.items()
    }

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=180,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

    return tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True,
    ).strip()


def respond(question):
    if not isinstance(question, str) or not question.strip():
        return "Please enter a health insurance question."

    question = question.strip()

    if len(question) > 2000:
        return "Your question is too long. Please keep it under 2,000 characters."

    if needs_plan_details(question):
        return plan_details_response()

    try:
        if BACKEND == "aws":
            return ask_sagemaker(question)

        if BACKEND == "local":
            return respond_local(question)

        return "Invalid inference backend configuration."

    except Exception as error:
        print(f"Inference error: {error}")

        try:
            import torch
            if isinstance(error, torch.cuda.OutOfMemoryError):
                torch.cuda.empty_cache()
                return "GPU memory is insufficient. Please try a shorter question."
        except ImportError:
            pass

        return "Sorry, something went wrong. Please try again."


if BACKEND == "local":
    load_local_model()
elif BACKEND == "aws":
    print("AWS SageMaker inference mode selected.")
else:
    raise ValueError(f"Unsupported inference backend: {BACKEND}")


with gr.Blocks(title="US Health Insurance AI Assistant") as demo:

    gr.Markdown(
        """
        # US Health Insurance AI Assistant

        Ask questions about US health insurance concepts.

        *Educational information only. Actual coverage depends on your insurance plan.*
        """
    )

    question = gr.Textbox(
        label="Your question",
        placeholder="Example: What is a health insurance deductible?",
        lines=3,
    )

    submit = gr.Button("Ask Question", variant="primary")

    answer = gr.Textbox(
        label="AI Assistant Response",
        lines=8,
        interactive=False,
    )

    submit.click(
        fn=respond,
        inputs=question,
        outputs=answer,
    )

    question.submit(
        fn=respond,
        inputs=question,
        outputs=answer,
    )


if __name__ == "__main__":
    demo.launch()
