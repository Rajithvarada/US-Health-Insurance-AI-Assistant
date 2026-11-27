# Phase 3 - Q&A Dataset Creation and Curation Report



## 1. Objective



Create a high-quality, source-supported US Health Insurance question-answer dataset for supervised fine-tuning.



The process included structural cleaning, source verification, answer accuracy review, answer correction, duplicate auditing, and final dataset validation.



## 2. Input and Structural Cleaning



\- Original structurally cleaned dataset: 4,990 records.

\- Unique QA IDs: 4,990.

\- Main file: `data/generated/qa\_dataset\_structural\_clean.csv`

\- Source collection: 215 source registry entries.

\- RAW dataset: 750 records.



Structural cleaning addressed repeated headers, malformed rows, and source/RAW reference relationships.



## 3. Answer Accuracy and Source Verification



Each reviewed answer was checked against its supporting source evidence.



\- Answer review log: 4,706 rows.

\- Revised answers verified and applied: 367.

\- Answer-accuracy rejections: 14.

\- RAW/source mapping errors in final validation: 0.

\- Unaccounted QA IDs: 0.



Corrections were applied to improve factual accuracy and source support.



## 4. Duplicate Review



Duplicate and redundancy checks were performed before finalizing the dataset.



\- Duplicate decision log: 199 rows.

\- Duplicate-review rejected records: 97.

\- Exact-match audit: 500 records.

\- Rejection overlap: 0.



Duplicate decisions were reconciled before final dataset creation.



## 5. Final Dataset Results



| Category | Records |

|---|---:|

| Original structurally clean dataset | 4,990 |

| Final curated dataset | 4,879 |

| Answer-accuracy rejections | 14 |

| Duplicate-review rejections | 97 |

| Total rejected | 111 |



The final curated dataset contains 4,879 eligible, unique Q&A pairs.



The confirmed instructor requirement was 4,500 valid Q&A pairs. The final dataset exceeded this requirement by 379 records.



## 6. Final Validation



\- Curated QA IDs: 4,879 unique.

\- Rejected QA IDs: 111 unique.

\- Total accounted records: 4,990.

\- Rejection overlap: 0.

\- RAW/source mapping errors: 0.

\- Unaccounted QA IDs: 0.

\- Finalization validation checks: Passed.



## 7. Final Output Files



\- `data/curated/qa\_dataset\_curated.csv`

\- `data/curated/qa\_dataset\_rejected.csv`

\- `data/curated/curation\_report.csv`

\- `phase3\_final\_summary.txt`



## 8. Completion Status



Phase 3 - Q&A Dataset Creation and Curation: \*\*COMPLETED\*\*



The final curated dataset of 4,879 eligible Q&A pairs was approved for Phase 4 preprocessing.




