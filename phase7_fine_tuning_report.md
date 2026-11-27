# Phase 7 – LLM Fine-Tuning Using QLoRA

## 1. Objective

Fine-tune the selected Qwen2.5-1.5B-Instruct base model using the curated US Health Insurance question-answer dataset.

QLoRA was used to make fine-tuning practical on hardware with limited GPU memory.

## 2. Base Model and Training Data

- Base model: Qwen/Qwen2.5-1.5B-Instruct
- Fine-tuning method: QLoRA
- Training dataset: `phase7/training/data/train_sft.jsonl`
- Validation dataset: `phase7/training/data/validation_sft.jsonl`
- Training records: 3,902
- Validation records: 489
- Random seed: 42

## 3. Training Configuration

| Parameter | Value |
|---|---:|
| LoRA rank | 8 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| Learning rate | 0.0001 |
| Epochs | 2 |
| Training batch size | 1 |
| Evaluation batch size | 1 |
| Gradient accumulation steps | 8 |
| Effective training batch size | 8 |
| Maximum sequence length | 256 |
| Warmup ratio | 0.05 |
| Weight decay | 0.01 |
| Optimizer | adamw_torch |
| Gradient checkpointing | Enabled |
| FP16 | Disabled |
| Evaluation strategy | Every epoch |
| Checkpoint saving | Every epoch |

## 4. Training Results

Training completed successfully with 976 optimizer steps.

| Metric | Epoch 1 | Epoch 2 |
|---|---:|---:|
| Global step | 488 | 976 |
| Validation loss | 0.708981 | 0.713383 |
| Mean token accuracy | 83.99% | 84.03% |

## 5. Training Observations

1. Both training epochs completed successfully.
2. Validation loss increased slightly during the second epoch.
3. Mean token accuracy improved marginally.
4. Epoch 1 had the lower validation loss.
5. These results indicated that further hyperparameter experiments and checkpoint evaluation were appropriate.

## 6. Model Artifacts

Important output locations:

- Training configuration: `phase7/configs/qlora_config.json`
- Training script: `phase7/training/train_qlora.py`
- Epoch 1 checkpoint: `phase7/checkpoints/qwen25_15b_qlora/checkpoint-488`
- Epoch 2 checkpoint: `phase7/checkpoints/qwen25_15b_qlora/checkpoint-976`
- Final adapter: `phase7/checkpoints/qwen25_15b_qlora_final`
- Merged model: `phase7/merged_model/qwen25_15b_merged`

The final adapter contains approximately 17.7 MB of adapter weights.

## 7. Subsequent Model Selection

Phase 7 used LoRA rank 8 as its original training configuration.

During Phase 8, additional experiments compared different learning rates and LoRA ranks. Experiment 3, using LoRA rank 4, was selected as the practical configuration based on its validation results and smaller adapter size.

The final project model was subsequently selected and evaluated during Phase 9. Therefore, the Phase 7 rank-8 adapter is not the final selected model.

## 8. Phase 7 Completion Status

- QLoRA training completed successfully.
- Two training epochs completed.
- Training and validation checkpoints generated.
- Final adapter saved.
- Merged model generated.
- Fine-tuned inference and model artifact verification performed.

**Phase 7: Completed.**