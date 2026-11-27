# Phase 4 - Dataset Preprocessing and Final Dataset Creation Report



## 1. Objective



Prepare the final curated US Health Insurance Q&A dataset for model fine-tuning by performing dataset inspection, leakage-safe grouping, train-validation-test splitting, instruction formatting, and structural validation.



## 2. Input Dataset



\- Input file: `data/curated/qa\_dataset\_curated.csv`

\- Total records: 4,879

\- Original curated dataset was preserved unchanged.



## 3. Preprocessing Activities



The following tasks were completed:



1\. Inspected dataset structure and content.

2\. Inspected source and RAW relationships.

3\. Reviewed four duplicate-question groups; all four groups were retained.

4\. Created leakage-safe groups using `source\_id` and normalized-question connections.

5\. Generated 197 leakage-safe groups.

6\. Performed group-aware 80:10:10 train-validation-test splitting.

7\. Investigated topic distribution.

8\. Completed text-quality audit.

9\. Converted records into instruction format.

10\. Generated train, validation, and test JSONL files.

11\. Completed final JSONL structural validation.



## 4. Dataset Split Results



| Split | Records | Percentage |

|---|---:|---:|

| Training | 3,902 | 79.98% |

| Validation | 489 | 10.02% |

| Testing | 488 | 10.00% |

| \*\*Total\*\* | \*\*4,879\*\* | \*\*100%\*\* |



## 5. Leakage Prevention



\- Total leakage-safe groups: 197.

\- Grouping considered source IDs and normalized-question relationships.

\- Related records were kept within the same split.

\- Leakage groups crossing splits: 0.



Source-level grouping was prioritized to reduce the risk of information leakage between training, validation, and test datasets.



## 6. JSONL Instruction Format



Each record uses the following model-neutral structure:



`{"instruction": "...", "input": "", "output": "..."}`



\- `instruction`: The user's health insurance question.

\- `input`: Empty additional context field.

\- `output`: The corresponding curated answer.



The intermediate format was later adapted to the selected model's chat template during model preparation.



## 7. Final Output Files



### JSONL datasets



\- `data/processed/train.jsonl`

\- `data/processed/validation.jsonl`

\- `data/processed/test.jsonl`



### Traceability files



\- `data/processed/train\_traceability.csv`

\- `data/processed/validation\_traceability.csv`

\- `data/processed/test\_traceability.csv`



### Split and grouping files



\- `data/processed/train\_split.csv`

\- `data/processed/validation\_split.csv`

\- `data/processed/test\_split.csv`

\- `data/processed/qa\_dataset\_with\_splits.csv`

\- `data/processed/qa\_dataset\_grouped.csv`



## 8. Validation Results



| Validation Check | Result |

|---|---:|

| JSON parsing errors | 0 |

| Missing or empty instruction/output | 0 |

| Record count mismatches | 0 |

| Duplicate QA IDs in source split audit | 0 |

| Leakage groups crossing splits | 0 |



The final JSONL structural validation passed.



## 9. Topic Distribution



\- Unique topics across the dataset: 771.

\- Topic coverage was not uniform across splits.

\- Source-level grouping was retained to prevent leakage.



## 10. Completion Status



Phase 4 - Dataset Preprocessing and Final Dataset Creation: \*\*COMPLETED\*\*



The final 4,879 records were successfully converted into train, validation, and test datasets for subsequent model development.




