
import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


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


def model_fn(model_dir):
    print("Loading tokenizer...")

    tokenizer = AutoTokenizer.from_pretrained(model_dir)

    print("Loading fine-tuned model...")

    model = AutoModelForCausalLM.from_pretrained(
        model_dir,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    model.eval()

    print(f"Model loaded successfully on {device}.")

    return {
        "model": model,
        "tokenizer": tokenizer
    }


def transform_fn(model_data, input_data, content_type, accept):
    if content_type != "application/json":
        raise ValueError("Only application/json requests are supported.")

    if isinstance(input_data, (bytes, bytearray)):
        input_data = input_data.decode("utf-8")

    if isinstance(input_data, str):
        request = json.loads(input_data)
    else:
        request = input_data

    question = request.get("question") or request.get("inputs")

    if not isinstance(question, str) or not question.strip():
        raise ValueError(
            "Please provide a non-empty question or inputs field."
        )

    model = model_data["model"]
    tokenizer = model_data["tokenizer"]

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question.strip()
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    inputs = {
        key: value.to(model.device)
        for key, value in inputs.items()
    }

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=180,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    answer = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True
    )

    response = {
        "answer": answer.strip()
    }

    return json.dumps(response), "application/json"
