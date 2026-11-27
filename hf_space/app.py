import os
import torch
import gradio as gr
import spaces

from transformers import AutoModelForCausalLM, AutoTokenizer
from safety import needs_plan_details, plan_details_response

MODEL_ID = os.getenv(
    "MODEL_ID",
    "rajith-ai-2003/us-health-insurance-ai-model"
)

SYSTEM_PROMPT = (
    "You are a US Health Insurance Educational Assistant. "
    "Explain US health insurance concepts accurately in simple English. "
    "Do not invent insurance rules or plan-specific coverage details. "
    "If information depends on a specific insurance plan, clearly say so. "
    "Provide educational information only."
)

model = None
tokenizer = None


def load_model():
    global model, tokenizer

    if model is not None:
        return

    print("Loading fine-tuned tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    print("Loading fine-tuned model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True
    )

    model.eval()
    print("Model loaded successfully.")


@spaces.GPU
def generate_answer(question):
    global model

    load_model()

    model.to("cuda")

    try:
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
            key: value.to("cuda")
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

    finally:
        model.to("cpu")
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def respond(question):
    if not isinstance(question, str) or not question.strip():
        return "Please enter a health insurance question."

    question = question.strip()

    if len(question) > 2000:
        return "Please keep your question under 2,000 characters."

    if needs_plan_details(question):
        return plan_details_response()

    try:
        return generate_answer(question)
    except Exception as error:
        print(f"Inference error: {error}")
        return "Sorry, the AI service is temporarily unavailable."


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
    demo.queue().launch()
