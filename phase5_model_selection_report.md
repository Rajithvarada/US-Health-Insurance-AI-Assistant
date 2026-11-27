# Phase 5 – Base Model Selection Report

## 1. Selected Base Model

- Model name: Qwen2.5-1.5B-Instruct
- Hugging Face ID: Qwen/Qwen2.5-1.5B-Instruct
- Organization: Alibaba Cloud (Qwen)
- Model type: Instruction-tuned causal language model
- Architecture: Qwen2ForCausalLM
- Model size: 1.5B parameter class

## 2. Technical Configuration

| Property | Verified value |
|---|---|
| Hidden size | 1536 |
| Transformer layers | 28 |
| Attention heads | 12 |
| Context length | 32768 tokens |
| Model config vocabulary | 151936 |
| Tokenizer vocabulary | 151665 |
| Tie word embeddings | True |
| License | Apache 2.0 |

## 3. Compatibility Verification

- Hugging Face Transformers import: PASS
- PEFT import: PASS
- Datasets import: PASS
- Accelerate import: PASS
- CUDA availability: PASS
- NVIDIA RTX 2050 detection: PASS
- Tokenizer loading: PASS
- Chat template availability: PASS
- apply_chat_template test: PASS
- Model configuration loading: PASS
- License metadata verification: PASS

Note: Full model weight loading and fine-tuning have not yet been tested.

## 4. Hardware Considerations

Available hardware:
- GPU: NVIDIA GeForce RTX 2050
- VRAM: 4 GB
- CPU: AMD Ryzen 7 7435HS

Estimated FP16 model weight memory is approximately 3 GB, excluding runtime overhead.

The available 4 GB VRAM is insufficient for dependable full fine-tuning. Cloud GPU execution is recommended for fine-tuning experiments. Local execution will be limited to compatible lightweight tests and experiments.

## 5. Alternatives Considered

1. Qwen2.5-7B-Instruct
   - Larger model with higher memory requirements.
   - Apache 2.0 license.
   - Cloud GPU required for practical fine-tuning.

2. Mistral-7B-Instruct-v0.3
   - 7B instruction-tuned model.
   - Apache 2.0 license.
   - Higher hardware requirements.

3. Qwen2.5-3B-Instruct
   - Larger than the selected 1.5B model.
   - Its Qwen Research License requires separate review before commercial use.

## 6. Selection Justification

Qwen2.5-1.5B-Instruct is selected as the base model for the US Health Insurance AI Assistant project because it provides a practical balance between model size, instruction-following capability, Hugging Face ecosystem compatibility, licensing, and available hardware.

Its tokenizer and chat template were successfully tested against the installed Transformers environment.

The model is a suitable starting point for domain-specific supervised fine-tuning using the project's curated health insurance Q&A dataset.

## 7. Evaluation Limitations

The model has not yet been benchmarked on the project's validation and test datasets.

Its actual answer accuracy, relevance, completeness, and hallucination rate must be evaluated after fine-tuning.

## 8. Final Decision

Selected Base Model: Qwen/Qwen2.5-1.5B-Instruct

Selection status: Selected, pending fine-tuning and evaluation.

Official model card:
https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct
