# Phase 10 – Local Gradio Application Test Report

## Application
- Interface: Gradio 6.32.0
- Base model: Qwen2.5-1.5B-Instruct
- Fine-tuned model: Phase 9 best checkpoint, Experiment 3 Rank 4, Epoch 1
- Inference: Local 4-bit quantization
- Model loading: Successful
- System prompt: Improved to reduce unsupported plan-specific assumptions
- Safety guard: Keyword-based plan-details check added to the Gradio application

## Initial Tests

| Test | Initial Result | Observation |
|---|---|---|
| Gradio interface launch | PASS | Local interface launched successfully |
| Model loading | PASS | Fine-tuned model loaded successfully |
| Deductible question | PASS | Response generated |
| Copayment vs coinsurance | PARTIAL | Initial explanation needed improvement |
| Out-of-pocket maximum | PARTIAL | One answer was mostly correct; another reversed the meaning |
| MRI coverage question | NEEDS IMPROVEMENT | Model assumed Medicare without user specifying it |
| Deductible calculation | PASS | Correct result: $800 |
| Exact premium question | PARTIAL | Did not clearly state that plan details were unavailable |
| Empty input validation | PASS | Clear validation message displayed |
| Long input validation | PASS | 2,001-character input rejected |
| Normal inference after validation | PASS | Model generated a response |

## Prompt and Safety Guard Improvements

- Updated the system prompt in `phase10/app/app.py`.
- Updated the system prompt in `phase10/code/inference.py`.
- Added a keyword-based `needs_plan_details()` guard in the Gradio application.
- The guard returns a clarification message for selected plan-specific coverage and cost questions.
- General educational questions and numerical calculations continue to use model inference.

## Latest Regression Tests After Safety Guard

| Test | Result | Observation |
|---|---|---|
| MRI coverage without plan details | PASS | Safety guard requested plan details instead of assuming Medicare |
| Exact monthly premium | PASS | Safety guard avoided inventing a premium |
| Deductible calculation | PASS | $1,000 - $200 = $800 |
| Copayment vs coinsurance | PASS | General explanation generated correctly |
| Deductible definition | PASS | General definition generated correctly |

Latest regression result: 5 out of 5 tests passed.

Note: These are a small set of manual regression tests, not proof of complete factual accuracy. The keyword-based guard only catches selected phrases and does not identify every possible plan-specific question.

## Error Handling
- Empty questions are rejected.
- Questions exceeding 2,000 characters are rejected.
- GPU out-of-memory errors are handled.
- Unexpected inference errors are caught and logged.
- Selected plan-specific questions receive a clarification response before model inference.

## Limitations
- The model can still produce unsupported or inaccurate insurance information.
- The keyword-based safety guard is not a comprehensive insurance question classifier.
- More varied questions and independent factual evaluation are required.
- Local testing does not confirm AWS endpoint deployment.
- AWS live inference has not been successfully tested.

## Final Local Application Status

- Local Gradio application: WORKING
- Local fine-tuned model integration: WORKING
- Local 4-bit inference: WORKING
- Input validation: TESTED
- Error handling: IMPLEMENTED
- Latest manual regression tests: 5/5 PASS

## AWS Deployment Status – November 26, 2026

- SageMaker GPU endpoint quota: APPROVED (ml.g5.xlarge quota: 2).
- SageMaker model: Registered successfully.
- Endpoint configuration: Created successfully.
- S3 model artifact upload: Completed.
- Endpoint creation request: Submitted.
- Endpoint deployment outcome: FAILED.
- Failure reason: InsufficientInstanceCapacity in ap-southeast-2 for ml.g5.xlarge.
- Endpoint deletion: SUCCESSFUL.
- Deletion verification: DescribeEndpoint confirmed that the endpoint no longer exists.
- AWS inference testing: NOT COMPLETED.
- Replacement endpoint: NOT CREATED.
- S3 model artifact and SageMaker model registration: Retained.
- AWS Support case: Open; billing clarification requested.

## Final Conclusion

The local US Health Insurance AI Assistant is operational and its latest five manual regression tests passed. AWS infrastructure preparation was completed, but live SageMaker endpoint deployment was unsuccessful because of insufficient compute capacity. AWS live inference remains pending.
