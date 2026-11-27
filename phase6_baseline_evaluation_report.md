# Phase 6 – Baseline Model Evaluation Report

## 1. Evaluation Overview

- **Base model:** Qwen/Qwen2.5-1.5B-Instruct
- **Evaluation method:** Prompting only (no fine-tuning)
- **System prompt:** system_prompt_v1.txt
- **Prompt version:** v1
- **Evaluation sample:** 100 questions
- **Question source:** Validation split
- **Sampling seed:** 42
- **Generation status:** 100 successful, 0 failed
- **Maximum new tokens:** 300
- **Sampling:** do_sample=False
- **Test split:** Not used; reserved for final evaluation.

## 2. Dataset Audit

| Validation | Result |
|---|---:|
| Total records | 100 |
| Unique QA IDs | 100 |
| Missing QA IDs | 0 |
| Missing evaluation scores | 0 |
| Successful generations | 100 |
| Failed generations | 0 |

All 100 evaluation records passed the structural audit.

## 3. Baseline Evaluation Metrics

Scores use a 0–2 scale:

- 0 = Poor or incorrect
- 1 = Partially satisfactory
- 2 = Good or satisfactory

Normalized percentage = (average score / 2) × 100.

| Dimension | Score 0 | Score 1 | Score 2 | Average | Normalized |
|---|---:|---:|---:|---:|---:|
| Correctness | 30 | 65 | 5 | 0.75/2 | 37.5% |
| Relevance | 6 | 16 | 78 | 1.72/2 | 86.0% |
| Clarity | 0 | 1 | 99 | 1.99/2 | 99.5% |
| Consistency | 26 | 65 | 9 | 0.83/2 | 41.5% |

## 4. Overall Review Decisions

| Decision | Records |
|---|---:|
| needs_improvement | 97 |
| acceptable | 3 |

## 5. Model Limitations Identified

The manual review identified these recurring weaknesses:

1. Factual inaccuracies in Medicare coverage and eligibility explanations.
2. Incorrect or invented requirements, deadlines and qualifying conditions.
3. Confusion between Medicare Parts A and B and between different coverage programs.
4. Incorrect explanations of Marketplace eligibility and verification procedures.
5. Misleading statements about Premium Tax Credits and tax reconciliation.
6. Unsupported numerical thresholds, cost calculations and coverage limits.
7. Answers that contain a correct central statement but undermine it with inaccurate additional details.

## 6. Interpretation

The model demonstrates strong readability and generally good relevance, but its factual reliability is insufficient for the intended US health insurance educational assistant.

The baseline correctness score is 0.75/2 (37.5%).
The consistency score is 0.83/2 (41.5%).

These results indicate that prompting alone has not yet demonstrated adequate factual reliability for this project.

The evaluation sample was randomly selected from the validation split using seed 42. Its topic distribution was imbalanced, so the metrics should be interpreted as results for this sample rather than as a fully representative measurement across every insurance topic.

## 7. Unsupported-Claim Review Field

Non-empty reviewer commentary was found in 100 records in the unsupported_claims column.

This count represents populated review notes, not a binary count of confirmed unsupported factual claims. Individual notes must be interpreted alongside the answer and review decision.

## 8. Reproducibility and Data Protection

- Model: Qwen/Qwen2.5-1.5B-Instruct
- Prompt: system_prompt_v1.txt
- Generation configuration: do_sample=False, max_new_tokens=300
- Evaluation questions: evaluation_questions.csv
- Baseline outputs: baseline_model_outputs.csv
- Human review: baseline_review.csv
- Test split: preserved for final unbiased evaluation.

## 9. Phase 6 Conclusion

Baseline inference and human evaluation are complete for all 100 sampled questions.

Prompting alone produced readable and relevant answers, but factual correctness and consistency remain major limitations.

The baseline results will be used as the comparison reference for the fine-tuned model.

**Phase 6 status:** Evaluation completed; formal closure pending project progress update.
