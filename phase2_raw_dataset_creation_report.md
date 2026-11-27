\# Phase 2 – Raw Dataset Creation Report



\## 1. Objective



The objective of Phase 2 was to collect raw US health insurance information from the sources registered during Phase 1 and organize it into a structured dataset for subsequent question-answer generation and curation.



\## 2. Raw Dataset



\*\*File:\*\* `data/raw/raw\_data.csv`



\*\*Total raw records:\*\* 750



The dataset contains the following fields:



| Field | Description |

|---|---|

| raw\_id | Unique raw record identifier |

| source\_id | Reference to the registered source |

| source\_name | Name of the source |

| source\_url | Original source URL |

| topic | Subject category |

| extracted\_text | Collected information |

| collected\_date | Date recorded for collection |

| verification\_status | Verification status of the record |



\## 3. Verification Status



The raw dataset contains the following verification statuses:



| Status | Records |

|---|---:|

| Verified | 83 |

| Pending | 667 |

| \*\*Total\*\* | \*\*750\*\* |



Not all collected records had completed verification at this stage. Pending records were retained with their status clearly identified.



\## 4. Data Organization



Each raw record includes a unique identifier and a source reference. This structure helps trace collected information back to its registered source.



The dataset also records the topic, extracted text, collection date, and verification status to support later processing and quality checks.



\## 5. Topic Coverage



The raw dataset covers a broad range of US health insurance topics, including:



\- General health insurance concepts

\- Deductibles, copayments, and coinsurance

\- Health Savings Accounts

\- Health Insurance Marketplace

\- Medicare and Medicaid

\- Employer-sponsored health benefits

\- Prescription drug coverage

\- Provider networks

\- Appeals and consumer protections

\- Preventive healthcare

\- COBRA continuation coverage



\## 6. Output



The primary output of Phase 2 was:



`data/raw/raw\_data.csv`



The dataset contains 750 raw records collected from the registered source collection.



\## 7. Conclusion



Phase 2 – Raw Dataset Creation was completed with 750 structured raw records. Verification status was tracked separately, with 83 records marked verified and 667 marked pending. This raw dataset provided the input for subsequent Q\&A generation, curation, and preprocessing phases.

