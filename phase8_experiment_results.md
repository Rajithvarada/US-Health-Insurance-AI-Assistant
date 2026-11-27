# Phase 8 – Hyperparameter Tuning & Optimization

## Experiment 1 – Baseline Configuration

Model: Qwen/Qwen2.5-1.5B-Instruct
Training method: QLoRA
Training records: 3902
Validation records: 489
Completed epochs: 2
Total optimizer steps: 976
Random seed: 42

### Hyperparameter Configuration

| Hyperparameter | Value |
|---|---:|
| Learning rate | 0.0001 |
| Epochs | 2 |
| Train batch size | 1 |
| Evaluation batch size | 1 |
| Gradient accumulation steps | 8 |
| Effective training batch size | 8 |
| Warmup ratio | 0.05 |
| Weight decay | 0.01 |
| LoRA rank | 8 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |
| Maximum sequence length | 256 |
| Optimizer | adamw_torch |
| Gradient checkpointing | Enabled |
| FP16 | Disabled |

### Validation Results

| Metric | Epoch 1 | Epoch 2 |
|---|---:|---:|
| Validation loss | 0.708981 | 0.713383 |
| Mean token accuracy | 0.839888 | 0.840320 |
| Training steps | 488 | 976 |

### Observations

1. Validation loss increased slightly from epoch 1 to epoch 2.
2. Mean token accuracy improved marginally.
3. Epoch 2 did not demonstrate a clear validation-loss improvement.
4. Further experiments are required to identify a better configuration.

### Experiment Status

Completed. Retained as the baseline experiment.

This experiment is not yet declared the best configuration.

## Experiment 2 – Learning Rate 0.00005

- Learning Rate: 0.00005
- Epochs: 2
- Optimizer Steps: 976
- LoRA Rank: 8
- LoRA Alpha: 16
- LoRA Dropout: 0.05
- Batch Size: 1
- Gradient Accumulation: 8
- Warmup Steps: 49
- Weight Decay: 0.01
- Max Sequence Length: 256

### Validation Results

- Validation Loss: 0.72366655
- Mean Token Accuracy: 0.83815039 (83.82%)
- Training Status: Completed Successfully

### Comparison with Experiment 1

| Metric | Experiment 1 | Experiment 2 |
|---|---:|---:|
| Learning Rate | 0.0001 | 0.00005 |
| Validation Loss | 0.71338320 | 0.72366655 |
| Mean Token Accuracy | 84.03% | 83.82% |

Experiment 1 performed better on both validation loss and mean token accuracy.
Reducing the learning rate to 0.00005 did not improve validation performance.


## Experiment 3 – LoRA Rank 4

- Learning Rate: 0.0001
- Epochs: 2
- Optimizer Steps: 976
- LoRA Rank: 4
- LoRA Alpha: 16
- LoRA Dropout: 0.05
- Batch Size: 1
- Gradient Accumulation: 8
- Warmup Steps: 49
- Weight Decay: 0.01
- Maximum Sequence Length: 256

### Validation Results

- Validation Loss: 0.71287775
- Mean Token Accuracy: 0.84004798 (84.00%)
- Training Status: Completed Successfully
- Final Adapter: phase8/checkpoints/experiment_3_rank4_final

## Final Experiment Comparison

| Metric | Experiment 1 | Experiment 2 | Experiment 3 |
|---|---:|---:|---:|
| Learning Rate | 0.0001 | 0.00005 | 0.0001 |
| LoRA Rank | 8 | 8 | 4 |
| Validation Loss | 0.71338320 | 0.72366655 | 0.71287775 |
| Mean Token Accuracy | 84.03% | 83.82% | 84.00% |

### Observations

1. Experiment 2 performed worse than Experiment 1 on both validation metrics.
2. Experiment 3 achieved the lowest validation loss.
3. Experiment 1 achieved the highest mean token accuracy.
4. The difference between Experiments 1 and 3 is very small.
5. Reducing LoRA rank from 8 to 4 maintained nearly the same validation performance with fewer trainable adapter parameters.
6. No additional full training experiment was conducted.

## Best Hyperparameter Configuration – Selected

Experiment 3 is selected as the practical configuration because it achieved the lowest validation loss and nearly matched the highest token accuracy with a smaller LoRA rank.

| Hyperparameter | Selected Value |
|---|---:|
| Learning Rate | 0.0001 |
| Epochs | 2 |
| Per-device Batch Size | 1 |
| Gradient Accumulation Steps | 8 |
| Effective Batch Size | 8 |
| Warmup Steps | 49 |
| Weight Decay | 0.01 |
| LoRA Rank | 4 |
| LoRA Alpha | 16 |
| LoRA Dropout | 0.05 |
| Maximum Sequence Length | 256 |
| Optimizer | adamw_torch |
| Gradient Checkpointing | Enabled |
| FP16 | Disabled |
| Quantization | 4-bit NF4 with double quantization |
| Random Seed | 42 |

### Selection Note

The selected configuration is based on validation loss, mean token accuracy, and adapter efficiency. The improvement over Experiment 1 is marginal, not a substantial quality gain. Final answer quality must still be assessed separately; validation token accuracy is not equivalent to answer correctness.

## Phase 8 Status

Hyperparameter tuning experiments completed.

- Experiment 1: Baseline configuration.
- Experiment 2: Learning-rate experiment.
- Experiment 3: LoRA-rank experiment.
- Best Hyperparameter Configuration: Documented.
- Experiment Results: Documented.

The untouched test split remains reserved for final model evaluation.

