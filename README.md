# US Health Insurance AI Assistant

An educational AI assistant built using a fine-tuned Large Language Model (LLM) to answer questions about US health insurance.

This project demonstrates an end-to-end LLM development workflow, including data collection, dataset curation, preprocessing, baseline evaluation, QLoRA fine-tuning, hyperparameter optimization, final model evaluation, and application development.

## 1. Project Objectives
	
- Collect information from US health insurance sources.
- Build and curate a question-answer dataset.
- Prepare training, validation, and test datasets.
- Evaluate a pre-trained LLM before fine-tuning.
- Fine-tune the model using QLoRA.
- Experiment with hyperparameters.
- Select the best model checkpoint.
- Evaluate the model using quantitative metrics and manual review.
- Compare base-model and fine-tuned-model performance.
- Build a Gradio application for interacting with the fine-tuned model.
- Prepare the application for AWS SageMaker deployment.

## 2. Base Model

- Model: Qwen2.5-1.5B-Instruct
- Model provider: Qwen
- Fine-tuning method: QLoRA
- Selected experiment: Experiment 3
- LoRA rank: 4
- LoRA alpha: 16
- LoRA dropout: 0.05
- Selected checkpoint: Epoch 1

The Epoch 1 checkpoint was selected based on its validation performance.

## 3. Dataset

The dataset was curated from US health insurance information sources.

| Dataset | Records |
|---|---:|
| Source registry | 215 |
| Raw records | 750 |
| Structurally clean Q&A records | 4,990 |
| Final curated Q&A records | 4,879 |
| Training dataset | 3,902 |
| Validation dataset | 489 |
| Test dataset | 488 |

The final curated dataset contains 4,879 eligible Q&A pairs. Dataset splitting used leakage-safe grouping to keep related records within the same split.

The test dataset was kept separate from training and hyperparameter tuning.

## 4. Project Workflow

The project follows 11 phases:

1. Source Collection
2. RAW Dataset Creation
3. Q&A Creation and Curation
4. Dataset Preprocessing
5. Base Model Selection
6. Baseline Model Evaluation â€“ Prompting First
7. Fine-Tuning
8. Hyperparameter Tuning and Optimization
9. Model Validation and Final Evaluation
10. AWS Deployment and Final Application
11. Project Documentation and Interview Preparation

Phases 1â€“10 have been completed, including successful AWS SageMaker GPU deployment and real cloud inference testing.

Phase 11 documentation and interview preparation are in progress.

## 5. Technologies Used

### Model development and fine-tuning
- Python 3.10
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- PEFT
- TRL
- Accelerate
- BitsAndBytes

### Data processing and evaluation
- Pandas
- NumPy
- ROUGE
- BERTScore

### Application and AWS
- Gradio
- Boto3
- Amazon S3
- Amazon SageMaker
- AWS CLI

## 6. Fine-Tuning Configuration

The selected Experiment 3 configuration:

| Parameter | Value |
|---|---:|
| Base model | Qwen2.5-1.5B-Instruct |
| Fine-tuning | QLoRA |
| LoRA rank | 4 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |
| Learning rate | 0.0001 |
| Epochs | 2 |
| Batch size | 1 |
| Gradient accumulation | 8 |
| Maximum sequence length | 256 |
| Weight decay | 0.01 |
| Warmup steps | 49 |
| Optimizer | AdamW |
| Random seed | 42 |

The best checkpoint was selected from Epoch 1 based on validation performance.

## 7. Final Evaluation Results

The selected Epoch 1 checkpoint was evaluated on the untouched test dataset. A random sample of 100 answers was manually reviewed.

| Metric | Result |
|---|---:|
| Strict answer correctness | 21% |
| At least partially correct | 60% |
| Relevance | 85% |
| Claim-level precision | 36.78% |
| Reference-claim recall | 32.86% |
| Project-specific F1-style score | 34.71% |
| Unsupported-by-reference claim rate | 63.22% |
| ROUGE-1 F1 | 0.3136 |
| ROUGE-2 F1 | 0.0903 |
| ROUGE-L F1 | 0.2497 |
| BERTScore F1 | 0.7540 |
| Validation perplexity | 2.0283 |

### Evaluation Notes

- Strict correctness measures fully correct answers.
- Partial correctness includes answers that contain some correct information but are incomplete.
- Precision and recall are based on manually reviewed factual claims.
- The project-specific F1-style score is the harmonic mean of these two claim-level metrics.
- Unsupported-by-reference claims are not necessarily false; they are claims not established by the supplied reference answers.
- ROUGE measures lexical overlap, while BERTScore measures semantic similarity. Neither independently proves factual correctness.

The evaluation indicates that the model produces relevant answers, but factual correctness and unsupported claims remain important limitations.

## 8. Application Development and AWS Deployment

### Gradio Application

A Gradio interface was developed for the US Health Insurance AI Assistant.

Implemented features:

- Accept user health insurance questions.
- Generate answers using the selected fine-tuned model.
- Support local 4-bit model inference.
- Support an AWS SageMaker inference backend.
- Validate empty questions.
- Enforce a 2,000-character question limit.
- Handle invalid backend configurations.
- Handle missing AWS endpoint configuration.
- Handle inference failures and GPU memory errors.
- Apply a shared safety module for selected plan-specific questions.

### Local Application and Safety Testing

- Local Gradio application launched successfully.
- Local fine-tuned model loaded successfully using 4-bit quantization.
- Safety regression tests: 7/7 passed.
- Gradio UI regression tests: 5/5 passed.
- Error-handling tests: 5/5 passed.

Detailed reports are listed in Section 12 of this README.
### AWS Deployment Status

AWS deployment was successfully completed and tested using Amazon SageMaker AI.

Deployment configuration:

- AWS Region: `ap-southeast-2` (Asia Pacific â€“ Sydney)
- Model: Fine-tuned Qwen2.5-1.5B-Instruct
- SageMaker instance: `ml.g6.xlarge`
- GPU count: 1
- Endpoint name: `us-health-insurance-ai-endpoint-g6`
- Model artifact stored in Amazon S3.

Deployment milestones:

- Configured the AWS IAM execution role.
- Created an Amazon S3 bucket and uploaded the model artifact.
- Registered the model in SageMaker.
- Created an endpoint configuration.
- Successfully deployed the model using an `ml.g6.xlarge` GPU instance.
- Verified that the endpoint reached `InService`.
- Integrated SageMaker Runtime inference using Boto3.
- Successfully tested real cloud inference with a health insurance question.
- Deleted the endpoint after successful testing to prevent continued GPU endpoint runtime charges.

**Current status:**

- AWS model deployment: Successfully tested.
- Real-time cloud inference: Successfully tested.
- SageMaker endpoint: Deleted after testing.
- S3 model artifact: Retained.
- SageMaker model and endpoint configurations: Retained.
- Live AWS inference: Requires endpoint redeployment.

AWS billing and credit usage should be monitored because billing data may take time to update.

The earlier `ml.g5.xlarge` deployment attempt failed due to insufficient instance capacity. The subsequent `ml.g6.xlarge` deployment succeeded.

## 9. Hardware and Environment

Development hardware:

- NVIDIA GeForce RTX 2050
- 4 GB GPU VRAM
- CUDA-enabled PyTorch
- Windows operating system

QLoRA and 4-bit quantization were used to make fine-tuning practical with limited GPU memory.

## 10. Project Structure

```text
US_Health_Insurance_AI/
|
|-- data/
|   |-- Raw/
|   |-- Backups/
|   |-- generated/
|   |-- curated/
|   `-- Processed/
|
|-- phase6/
|   |-- prompts/
|   `-- evaluation/
|
|-- phase7/
|   |-- configs/
|   |-- training/
|   |-- logs/
|   |-- checkpoints/
|   `-- merged_model/
|
|-- phase8/
|   |-- configs/
|   |-- training/
|   |-- evaluation/
|   `-- checkpoints/
|
|-- phase9/
|   |-- checkpoints/
|   `-- evaluation/
|
|-- phase10/
|   |-- AWS_DEPLOYMENT.md
|   |-- app/
|   |-- code/
|   `-- model/
```
Note: Local model weights, checkpoints, virtual environments, and AWS credentials should not be uploaded to a public repository.

## 11. Setup Instructions

1. Install Python 3.10.
2. Clone or download the project.
3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Install a PyTorch build compatible with your GPU and CUDA environment.
6. Install the remaining dependencies:

```bash
pip install -r requirements.txt
```

7. Download or access the selected base model through Hugging Face.
8. Ensure the required local model artifacts are available.
9. Run the local Gradio application from the project root:

```bash
python -m phase10.app.app
```

10. Open the local URL displayed in the terminal.

For AWS inference, configure valid AWS credentials and set the SageMaker endpoint name before selecting the AWS backend. The model was successfully deployed and tested on Amazon SageMaker. The endpoint was deleted after testing, so redeployment is required before using live AWS inference.

Note: GPU, CUDA, PyTorch, and BitsAndBytes compatibility depends on the operating system and hardware. The requirements file does not install the CUDA-specific PyTorch build.

## 12. Documentation and Reports

Detailed project documentation is maintained in the repository root.

### Phase 1–9 Reports

- `phase1_source_collection_report.md`
- `phase2_raw_dataset_creation_report.md`
- `phase3_dataset_curation_report.md`
- `phase4_preprocessing_report.md`
- `phase5_model_selection_report.md`
- `phase6_baseline_evaluation_report.md`
- `phase7_fine_tuning_report.md`
- `phase8_experiment_results.md`
- `phase9_final_evaluation_report.md`

### Phase 10 Reports

- `phase10_aws_deployment_report.md`
- `phase10_error_handling_report.md`
- `phase10_local_gradio_test_report.md`
- `phase10_safety_regression_report.md`

**Total: 13 reports covering Phases 1–10.**

The architecture documentation is available in `architecture.md` and uses Mermaid.

## 13. Limitations and Responsible Use

- This is an educational project, not a production healthcare application.
- Model answers may contain incomplete or unsupported information.
- Insurance coverage and eligibility depend on individual plans and circumstances.
- Outputs must not be treated as official coverage, eligibility, or medical decisions.
- The current evaluation identifies factual accuracy and unsupported claims as areas requiring improvement.
- The AWS SageMaker endpoint was successfully deployed and tested using an `ml.g6.xlarge` GPU instance. It was deleted after successful inference testing. Live AWS inference requires redeployment.
- Additional dataset refinement, factual verification, and model evaluation are needed before real-world use.

## Author

Developed as a hands-on Generative AI and LLM fine-tuning project.
