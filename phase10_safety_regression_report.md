\# Phase 10 – Safety Regression Test Report



\## 1. Objective

Verify that the common safety module identifies selected plan-specific health insurance questions and allows general educational questions.



\## 2. Implementation

\- Created `phase10/app/safety.py`.

\- Added `needs\_plan\_details()` to identify selected plan-specific questions.

\- Added `plan\_details\_response()` for clarification messages.

\- Integrated the common safety module with:

&#x20; - `phase10/app/app.py`

&#x20; - `phase10/app/aws\_endpoint.py`



\## 3. Regression Test Results



| Test Case | Expected Result | Actual Result |

|---|---|---|

| MRI coverage | Require plan details | PASS |

| Exact monthly health insurance premium | Require plan details | PASS |

| Personal copay | Require plan details | PASS |

| Deductible definition | Allow general question | PASS |

| Copay vs coinsurance | Allow general question | PASS |

| Deductible calculation | Allow general question | PASS |

| Exact monthly health insurance premium | Require plan details | PASS |



\## 4. Summary



\- Total test cases: 7

\- Passed: 7

\- Failed: 0

\- Result: 7/7 PASS



\## 5. Limitation

The safety guard uses keyword matching. It only detects selected phrases and does not guarantee detection of every plan-specific question.



\## 6. Conclusion

The common safety module was successfully integrated into both local and AWS Gradio inference paths. All seven manual regression tests passed.



\## 7. Gradio UI Verification



\- MRI coverage clarification: PASS

\- Deductible definition: PASS

\- Deductible calculation: PASS

\- Copayment vs coinsurance: PASS

\- Exact monthly premium clarification after keyword update: PASS



UI regression result: 5/5 passed.

