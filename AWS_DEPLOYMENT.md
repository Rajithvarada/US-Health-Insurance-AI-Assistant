# AWS Deployment Documentation

## 1. Project Overview

Project: US Health Insurance AI Assistant

Cloud Platform: Amazon Web Services (AWS)

Deployment Service: Amazon SageMaker AI

AWS Region: Asia Pacific (Sydney) — `ap-southeast-2`

## 2. AWS Resources

| Resource | Configuration |
|---|---|
| S3 Bucket | `us-health-insurance-ai-2026-667455045498-ap-southeast-2-an` |
| Model Artifact | `s3://us-health-insurance-ai-2026-667455045498-ap-southeast-2-an/model.tar.gz` |
| SageMaker Model | `us-health-insurance-ai-model` |
| Execution Role | `USHealthInsuranceSageMakerExecutionRole` |
| Instance Type | `ml.g6.xlarge` |
| GPU Count | 1 |

## 3. Model Deployment

- Created an Amazon SageMaker model.
- Configured the Hugging Face PyTorch inference container.
- Created an endpoint configuration.
- Deployed the model using an `ml.g6.xlarge` GPU instance.
- Endpoint name: `us-health-insurance-ai-endpoint-g6`.

## 4. Inference Testing

Successfully tested the deployed model using the SageMaker Runtime API.

Test Question:

"What is a deductible in health insurance?"

The model returned an explanation describing a deductible as the amount a person pays before the insurer begins paying its share of covered healthcare costs.

**Result: PASS**

This confirmed that the deployed model successfully performed cloud-based inference.

## 5. Application Integration

Integrated SageMaker Runtime inference into:

`phase10/app/aws_endpoint.py`

The application:
- Validates user questions.
- Checks plan-specific questions using the safety module.
- Invokes the SageMaker endpoint.
- Parses the model response.
- Handles inference errors.

## 6. Cost Management

- Verified AWS credits in the Billing dashboard.
- Deleted the SageMaker endpoint after successful inference testing to prevent continued GPU endpoint runtime charges.
- Retained the S3 model artifact and SageMaker model resources for future deployment.
- Billing and credit usage should be checked again after AWS usage data updates.

## 7. Deployment Status

**Cloud deployment and inference test: SUCCESSFUL**

**SageMaker endpoint: DELETED after testing**

The endpoint must be deployed again before using live SageMaker inference.

## 8. Important Notes

- Never store AWS access keys, secret keys, passwords, or other credentials in this documentation.
- The model artifact is retained in Amazon S3.
- The endpoint configuration and SageMaker model are retained.
- AWS charges may still apply to retained storage and other resources.