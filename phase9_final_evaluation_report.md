# US Health Insurance AI Assistant
## Phase 9 – Model Validation & Final Evaluation Report

**Evaluation date:** 2026-11-24  
**Project:** US Health Insurance AI Assistant using LLM Fine-Tuning

---

## 1. Executive Summary

This phase evaluated the fine-tuned US Health Insurance AI Assistant using validation and untouched test data. The selected model is Qwen/Qwen2.5-1.5B-Instruct, fine-tuned using QLoRA.

The best checkpoint was selected from Experiment 3 (Rank 4), based on validation loss and token accuracy.

The selected checkpoint generated answers for all 488 records in the untouched test dataset. A random sample of 100 answers (seed 42) was manually reviewed and used for answer-level and claim-level evaluation.

The evaluation identified useful improvements in some areas but also significant limitations in factual correctness and unsupported claims. The model should therefore be treated as an educational prototype requiring further validation, not as an authoritative insurance decision system.

## 2. Model and Fine-Tuning Configuration

| Item | Configuration |
|---|---|
| Base model | Qwen/Qwen2.5-1.5B-Instruct |
| Fine-tuning method | QLoRA |
| Selected experiment | Experiment 3 |
| LoRA rank | 4 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| Learning rate | 0.0001 |
| Epochs | 2 |
| Per-device batch size | 1 |
| Gradient accumulation | 8 |
| Warmup steps | 49 |
| Weight decay | 0.01 |
| Maximum sequence length | 256 |
| Optimizer | adamw_torch |
| Training hardware | NVIDIA RTX 2050, 4 GB VRAM |

### Training results

| Metric | Epoch 1 | Epoch 2 |
|---|---:|---:|
| Training loss | 0.58656 | 0.58629 |
| Validation loss | 0.70719 | 0.71288 |
| Token accuracy | 84.06% | 84.00% |

Training completed successfully with 976 steps.

## 3. Hyperparameter Experiment Comparison

Three configurations were compared.

| Experiment | Main configuration difference | Validation loss | Token accuracy |
|---|---|---:|---:|
| Experiment 1 | Rank 8, LR 0.0001 | 0.71338 | 84.03% |
| Experiment 2 | Rank 8, LR 0.00005 | 0.72367 | 83.82% |
| Experiment 3 | Rank 4, LR 0.0001 | 0.71288 | 84.00% |

Experiment 3 was selected because it had the lowest validation loss and nearly the same token accuracy as Experiment 1, with fewer adapter parameters.

## 4. Best Checkpoint Selection

Two Experiment 3 checkpoints were compared:

| Checkpoint | Validation loss | Token accuracy |
|---|---:|---:|
| Epoch 1 – checkpoint-488 | 0.70719 | 84.06% |
| Epoch 2 – checkpoint-976 | 0.71288 | 84.00% |

**Selected checkpoint:** `phase9/checkpoints/best_checkpoint_epoch1`

Epoch 1 was selected because it had lower validation loss and slightly higher token accuracy.

A slight overfitting signal was observed in Epoch 2 because validation loss increased while training loss remained nearly stable. There was no strong evidence of underfitting.

## 5. Validation Evaluation

The selected Experiment 3 configuration's Epoch 2 final adapter was manually reviewed on 100 validation questions.

| Metric | Average score (0–2) |
|---|---:|
| Correctness | 0.98 |
| Relevance | 1.67 |
| Clarity | 2.00 |
| Consistency | 1.23 |

- Acceptable answers: 25/100.
- Answers needing improvement: 75/100.
- Answers flagged with unsupported claims: 49/100.

**Important:** This validation review used the Epoch 2 final adapter. It is not a human evaluation of the selected Epoch 1 checkpoint.

## 6. Untouched Test Dataset Evaluation

The untouched test dataset contained 488 records.

The selected Epoch 1 checkpoint generated:
- Successful outputs: 488
- Failed outputs: 0
- Unique QA IDs: 488
- Empty answers: 0
- Duplicate QA IDs: 0

All test outputs were generated using the selected checkpoint, the project system prompt v1, greedy decoding, and a maximum of 300 new tokens.

A random sample of 100 answers was selected using seed 42 for manual and metric-based evaluation. The remaining 388 outputs were preserved.

## 7. Answer-Level Factual Correctness

Manual correctness scoring used:
- 0 = Incorrect
- 1 = Partially correct
- 2 = Fully correct

| Result | Count | Percentage |
|---|---:|---:|
| Fully correct | 21 | 21% |
| Partially correct | 39 | 39% |
| Incorrect | 40 | 40% |
| Invalid or missing | 0 | 0% |

Strict answer-level correctness was **21%**.

Answers that were at least partially correct accounted for **60%** of the sample.

## 8. Claim-Level Precision

Precision was evaluated by manually checking factual claims against the corresponding reference answers.

| Metric | Result |
|---|---:|
| Total generated factual claims | 174 |
| Supported claims | 64 |
| Unsupported-by-reference claims | 110 |
| Claim-level precision | 36.78% |

Formula:

Supported claims / Total generated factual claims × 100

## 9. Reference-Fact Recall

Recall measured how many distinct important facts from the reference answers were covered by the generated answers.

| Metric | Result |
|---|---:|
| Total reference claims | 140 |
| Covered reference claims | 46 |
| Missed reference claims | 94 |
| Reference-fact recall | 32.86% |

Formula:

Covered reference claims / Total reference claims × 100

## 10. F1-Style Score

Using the measured precision and recall:

- Precision: 36.78%
- Recall: 32.86%
- F1-style harmonic mean: 34.71%

This is a project-specific harmonic mean. The precision and recall denominators represent different claim sets, so this should not be interpreted as a standardized classification F1 score.

## 11. Perplexity

The selected checkpoint's Epoch 1 validation loss was 0.7071877718.

Perplexity was calculated as:

Perplexity = exp(validation loss)

**Perplexity: 2.0283**

This is a token-level language-model metric. It does not establish factual correctness or answer quality.

## 12. ROUGE Evaluation

ROUGE was calculated on the 100-answer test sample using ROUGE-1, ROUGE-2, and ROUGE-L with stemming.

| Metric | Precision | Recall | F1 |
|---|---:|---:|---:|
| ROUGE-1 | 0.3234 | 0.3328 | 0.3136 |
| ROUGE-2 | 0.0956 | 0.0946 | 0.0903 |
| ROUGE-L | 0.2548 | 0.2670 | 0.2497 |

ROUGE measures lexical overlap with reference answers. It does not independently establish factual correctness.

## 13. BERTScore Evaluation

BERTScore was calculated on the same 100-answer test sample using `distilbert-base-uncased`, six layers, and no baseline rescaling.

| Metric | Mean score |
|---|---:|
| Precision | 0.7513 |
| Recall | 0.7582 |
| F1 | 0.7540 |

BERTScore measures semantic similarity. A high semantic similarity score does not guarantee that an answer is factually correct.

## 14. Factual Correctness and Relevance

The answer-level correctness results were reused from the manual review in Step 7; no duplicate review was performed.

- Fully correct answers: 21%.
- Partially correct answers: 39%.
- Incorrect answers: 40%.

Relevance was separately reviewed on the same 100 test answers.

| Relevance score | Count | Percentage |
|---|---:|---:|
| Relevant (2) | 72 | 72% |
| Partially relevant (1) | 26 | 26% |
| Irrelevant (0) | 2 | 2% |

- Average relevance: 1.70 / 2.
- Normalized relevance: 85.00%.
- At least partially relevant: 98%.

Relevance measures whether an answer addresses the question. It does not establish that the answer is correct.

## 15. Hallucination and Unsupported-Claim Evaluation

The same 100-answer test sample was used for claim-level review.

| Metric | Result |
|---|---:|
| Total factual claims | 174 |
| Supported claims | 64 |
| Unsupported-by-reference claims | 110 |
| Unsupported-by-reference claim rate | 63.22% |
| Answers with at least one unsupported claim | 79/100 (79%) |
| Answers with zero unsupported claims | 21/100 (21%) |

An unsupported claim is not necessarily false. It may be additional information that is not established by the supplied reference answer. These results are reference-based unsupported-claim indicators, not independently verified hallucination labels.

## 16. Base Model vs Fine-Tuned Model

The base and fine-tuned models were compared using the same 100 validation questions, matching QA IDs, the same base model, prompt v1, maximum 300 new tokens, and greedy decoding.

| Metric | Base model | Fine-tuned model | Difference |
|---|---:|---:|---:|
| Correctness | 0.750 | 0.980 | +0.230 |
| Relevance | 1.720 | 1.670 | -0.050 |
| Clarity | 1.990 | 2.000 | +0.010 |
| Consistency | 0.830 | 1.230 | +0.400 |
| Acceptable review decisions | 3/100 | 25/100 | +22 percentage points |

The reviewed fine-tuned model showed higher average correctness and consistency, nearly unchanged clarity, and slightly lower relevance on this validation sample.

**Comparison limitations:**
- The fine-tuned human-review file used the Experiment 3 Epoch 2 final adapter, not the selected Epoch 1 checkpoint.
- The baseline and fine-tuned `unsupported_claims` fields used different formats, so their counts were not directly compared.
- These results apply to the reviewed 100-question validation sample and do not prove universal improvement.

## 17. Overall Findings

### Positive findings
- Fine-tuning and QLoRA training completed successfully on the available GPU.
- The selected checkpoint was preserved and successfully used for inference.
- All 488 untouched test records received generated answers.
- Test-set relevance was 85%.
- The validation comparison showed improvements in average correctness and consistency for the reviewed fine-tuned adapter.

### Areas requiring improvement
- Strict answer-level correctness was 21% on the reviewed test sample.
- Claim-level precision was 36.78%.
- Reference-fact recall was 32.86%.
- 79% of reviewed answers contained at least one unsupported-by-reference claim.
- Fine-tuning did not improve relevance in the validation comparison.

### Recommended future improvements
- Improve the training dataset's factual coverage and answer quality.
- Strengthen instructions against unsupported details and invented plan-specific values.
- Add reference-grounded answer generation and retrieval support.
- Evaluate the selected Epoch 1 checkpoint with a separate human-reviewed validation comparison before making checkpoint-specific quality claims.
- Perform further evaluation with a larger, independently reviewed test sample.
- Add safeguards for plan-specific, eligibility, and coverage questions.

## 18. Final Conclusion

The US Health Insurance AI Assistant was successfully fine-tuned and evaluated using a structured validation and test workflow.

The selected checkpoint is `best_checkpoint_epoch1`, chosen using validation loss and token accuracy. It successfully generated answers for all 488 untouched test records.

The evaluation shows that the model can produce relevant and readable responses, but factual correctness, reference coverage, and unsupported-claim control remain important weaknesses.

Therefore, the project demonstrates a working LLM fine-tuning and evaluation pipeline, but the model is not yet reliable enough for unsupervised health insurance guidance or official coverage and eligibility decisions.

**Final status:** Fine-tuning and evaluation implementation completed. Further model-quality improvement and validation are recommended before deployment.
