# \# Phase 10 – AWS Deployment Report

# 

# \## 1. Project

# \*\*Project Name:\*\* US Health Insurance AI Assistant

# 

# \## 2. AWS Configuration

# \- AWS Region: ap-southeast-2 (Asia Pacific – Sydney)

# \- AWS Service: Amazon SageMaker AI

# \- S3 Bucket: `us-health-insurance-ai-2026-667455045498-ap-southeast-2-an`

# \- SageMaker Model: `us-health-insurance-ai-model`

# \- IAM Execution Role: `USHealthInsuranceSageMakerExecutionRole`

# \- Model Artifact: `s3://us-health-insurance-ai-2026-667455045498-ap-southeast-2-an/model.tar.gz`

# 

# \## 3. Completed AWS Setup

# \- AWS account created and accessed successfully.

# \- AWS CLI configured and authenticated.

# \- IAM execution role created with required permissions.

# \- S3 bucket created with public access blocked and server-side encryption.

# \- Fine-tuned model archive uploaded to Amazon S3.

# \- SageMaker model registered successfully.

# \- SageMaker endpoint configurations created successfully.

# \- AWS service quotas reviewed.

# \- AWS promotional credits and budget alert reviewed.

# 

# \## 4. Model Artifact

# \- Base Model: Qwen2.5-1.5B-Instruct.

# \- Fine-tuning Method: QLoRA.

# \- Selected Checkpoint: Phase 9 best checkpoint, Phase 8 Experiment 3.

# \- LoRA Rank: 4.

# \- LoRA Alpha: 16.

# \- Selected Epoch: 1.

# \- Merged Model Format: FP16.

# \- Model Archive: `model.tar.gz`.

# \- Approximate Archive Size: 2.59 GB.

# \- S3 Upload: Successful.

# 

# \## 5. Initial Deployment Attempt – G5 Instance

# \- Instance Type: `ml.g5.xlarge`.

# \- AWS Region: `ap-southeast-2`.

# \- Endpoint deployment request submitted.

# \- Deployment failed due to `InsufficientInstanceCapacity`.

# \- This was an AWS compute-capacity issue.

# \- No model-code failure was established from this deployment attempt.

# \- Failed endpoint deletion was confirmed.

# \- S3 model archive and SageMaker model registration were retained.

# 

# \## 6. Successful Deployment – G6 Instance

# 

# After the G5 capacity issue, a replacement deployment was completed using a G6 GPU instance.

# 

# \- Instance Type: `ml.g6.xlarge`.

# \- AWS Region: `ap-southeast-2`.

# \- Endpoint Name: `us-health-insurance-ai-endpoint-g6`.

# \- Endpoint Configuration: `us-health-insurance-ai-endpoint-config-copy-11-27`.

# \- Initial Instance Count: 1.

# \- Endpoint successfully reached `InService` status.

# \- Successful real-time inference test completed.

# 

# \### 6.1 Cloud Inference Test

# 

# \*\*Test Question:\*\*

# 

# What is a deductible in health insurance?

# 

# \*\*Model Response:\*\*

# 

# A deductible is the amount of money that must be paid before an insurer begins paying its share of covered healthcare costs for a person enrolled in certain types of private health insurance. The exact amount can vary by type of coverage and state requirements.

# 

# \*\*Result:\*\* Successful.

# 

# This confirmed that the fine-tuned model could perform real-time inference through an actual Amazon SageMaker GPU endpoint.

# 

# \## 7. Endpoint Cleanup

# After successful inference testing:

# 

# \- SageMaker G6 endpoint deletion was initiated.

# \- Endpoint deletion was confirmed.

# \- Subsequent SageMaker Endpoints listing showed zero active endpoints.

# \- S3 model archive was retained.

# \- SageMaker model registration was retained.

# \- Endpoint configuration records were retained.

# 

# \*\*Current Endpoint Status:\*\* Inactive / Deleted.

# 

# Live AWS inference requires redeploying the SageMaker endpoint.

# 

# \## 8. Application Integration

# \- Created `phase10/app/aws\_endpoint.py` for SageMaker Runtime integration.

# \- Integrated AWS inference with the Gradio application.

# \- Implemented question validation.

# \- Added a 2,000-character input limit.

# \- Integrated shared safety checks.

# \- Added exception handling for AWS inference failures.

# \- Verified AWS integration module import successfully.

# \- Verified Gradio application import successfully.

# \- Verified local fine-tuned model loading successfully.

# 

# \*\*Note:\*\* The AWS endpoint is currently deleted. Therefore, live AWS inference through the application requires endpoint redeployment.

# 

# \## 9. Safety and Error Handling

# \### Safety Regression

# \- Seven manual safety regression tests completed.

# \- Result: 7/7 passed.

# \- Shared safety module integrated into local and AWS inference paths.

# 

# \### Error Handling

# \- Empty question validation tested.

# \- Questions exceeding 2,000 characters tested.

# \- Invalid inference backend handling tested.

# \- Missing AWS endpoint configuration handling tested.

# \- AWS inference failure handling tested.

# \- Result: 5/5 passed.

# 

# \### Gradio UI

# \- Local Gradio application import verified.

# \- UI regression tests: 5/5 passed.

# \- Local fine-tuned model loading verified.

# \- Plan-specific question safety behavior tested.

# 

# \## 10. Cost Management

# \- AWS promotional credits reported: $120.

# \- AWS budget alert: $1.00.

# \- G5 and G6 deployment attempts were performed in the Sydney region.

# \- The successful G6 endpoint was active temporarily for deployment and inference testing.

# \- The endpoint was deleted after testing to avoid ongoing GPU instance charges.

# \- S3 model artifact remains stored and may incur storage charges.

# \- Billing and credit information may take time to update.

# \- Final charges and credit usage must be verified in the AWS Billing dashboard.

# \- Promotional credits and pricing estimates do not guarantee zero actual charges.

# 

# \## 11. Deployment Challenges and Solutions

# 

# | Challenge | Resolution |

# |---|---|

# | G5 instance capacity unavailable | Switched to G6 instance |

# | Endpoint deployment delay | Monitored endpoint status |

# | Need to control GPU costs | Deleted endpoint after successful testing |

# | Endpoint inactive after testing | Documented redeployment requirement |

# 

# \## 12. Final Deployment Outcome

# 

# The following milestones were successfully completed:

# 

# \- AWS account and infrastructure setup.

# \- IAM role and permissions configuration.

# \- S3 bucket creation and model artifact upload.

# \- SageMaker model registration.

# \- Endpoint configuration creation.

# \- Successful G6 GPU endpoint deployment.

# \- Endpoint reached `InService`.

# \- Real-time inference using the fine-tuned model.

# \- Successful inference response received.

# \- Endpoint deletion and cleanup.

# \- Local Gradio and AWS integration verification.

# \- Safety and error-handling verification.

# 

# \### Final Status

# 

# \*\*AWS Deployment: SUCCESSFULLY TESTED\*\*

# 

# \*\*Real SageMaker GPU Inference: SUCCESSFUL\*\*

# 

# \*\*Current Endpoint Status: DELETED / INACTIVE\*\*

# 

# \*\*Live AWS Inference: Requires endpoint redeployment.\*\*

# 

# The project successfully demonstrated deployment and real-time inference of a fine-tuned language model using Amazon SageMaker. The endpoint was intentionally deleted after testing to avoid ongoing GPU instance costs, while the S3 model artifact and SageMaker model registration were retained.

