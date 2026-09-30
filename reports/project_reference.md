# Customer Experience and Retention Analysis

## 1. Project goal

The goal of this project is to study customer churn using the IBM Telco Customer Churn sample dataset and build a structured, statistics-first analysis workflow. The focus is not only prediction, but also understanding which customer patterns are associated with churn, how data quality issues are handled, and how findings can support retention strategy and future experimentation.

This project is designed to be interview-ready and reproducible. It follows a clear flow:

1. Validate the raw dataset.
2. Clean and document transformations.
3. Explore churn patterns with SQL and descriptive analysis.
4. Run statistical inference and hypothesis testing.
5. Build predictive models and compare model trade-offs.
6. Turn findings into business recommendations and experiment design.

The project is intentionally observational. We do not claim causality from the data alone. We speak in terms of associations and statistical evidence.

---

## 2. Why this project matters

Customer retention is a common business problem across subscription-based industries. A company may have healthy growth, but if retention is weak, revenue becomes unstable. This project uses churn analysis to answer practical questions such as:

- Which customer groups churn more often?
- Are month-to-month contracts riskier than long-term contracts?
- Do service-related features, payment methods, or tenure patterns matter?
- What is the business impact of churn by segment?

This analysis is useful for data science, analytics, and product or marketing teams because it connects customer behavior patterns to retention strategy.

---

## 3. Dataset and source

Dataset: IBM Telco Customer Churn sample dataset

Source: IBM sample data used in telco churn studies, also widely reused in Kaggle examples.

Key facts from the validation run:

- 7,043 rows
- 21 raw columns
- 1,869 churned customers
- 5,174 retained customers
- 11 blank TotalCharges values, all matched to tenure = 0
- 0 duplicate customer IDs
- 0 duplicate rows

This confirms the dataset is structurally sound for analysis after cleaning.

---

## 4. Project workflow

### Stage 1: Data ingestion and validation

Goal: confirm the raw data is valid and understand any obvious data quality issues before modeling.

Checks performed:

- row and column counts
- duplicate row detection
- duplicate customer ID detection
- category validation against allowed values
- logic validation for internet service and phone service rules
- review of blank TotalCharges and tenure = 0 cases
- review of unusual ratio checks between TotalCharges and tenure x MonthlyCharges

Key findings from the real data:

- No duplicate rows or duplicate customer IDs.
- No major category mismatch issues.
- 11 blank TotalCharges values were found.
- Those 11 rows were exactly the tenure = 0 customers.
- TotalCharges is strongly related to tenure x MonthlyCharges, so multicollinearity is expected later in modeling.

This stage is essential because it prevents false conclusions caused by malformed or inconsistent data.

### Stage 2: Cleaning and transformation

Goal: create a clean dataset while documenting each transformation.

Cleaning decisions:

- Fill blank TotalCharges with 0 for customers with tenure = 0.
- Convert tenure to integer.
- Convert MonthlyCharges and TotalCharges to numeric values.
- Recode SeniorCitizen from 0/1 to No/Yes for consistency.
- Add churn_flag to represent churn as a binary target.
- Preserve the original Churn column for traceability.

All transformations were recorded in the transformation log.

### Stage 3: SQL analysis and EDA

Goal: summarize churn patterns at the business level and identify segments that appear different.

The analysis uses SQLite and summary tables to review:

- overall churn rate
- average tenure
- average monthly charges
- churn by contract type
- churn by payment method
- churn by internet service
- churn by tenure segment

Verified results from the project:

- Overall churn rate: 26.54%
- Month-to-month churn: 42.71%
- One-year contract churn: 11.27%
- Two-year contract churn: 2.83%
- Fiber optic churn: 41.89%
- DSL churn: 18.96%
- No internet service churn: 7.40%
- 0 to 12 month tenure churn: 47.44%
- 49+ month tenure churn: 9.51%

These findings show that contract type, internet service, and tenure are likely useful segments for churn analysis.

### Stage 4: Statistical inference

Goal: test specific hypotheses and quantify uncertainty.

Planned or intended questions:

- Do month-to-month customers have different churn rates than longer-term customers?
- Do churned customers differ from retained customers on monthly charges and tenure?
- Are service combinations associated with churn differences?

Methods considered include:

- chi-square tests for categorical comparisons
- t-tests or Welch tests for average differences
- non-parametric tests if assumptions fail
- effect sizes and confidence intervals

This stage is designed to go beyond descriptive observation and bring statistical evidence into the analysis.

### Stage 5: Bootstrapping and permutation

Goal: estimate uncertainty and test the robustness of observed patterns without relying on strict assumptions.

Bootstrap helps estimate confidence intervals for:

- churn-rate differences by group
- mean tenure differences
- monthly charge differences

Permutation tests can assess whether a churn difference could arise from random label shuffling under the null hypothesis.

This is useful because real-world customer data often violates strict statistical assumptions.

### Stage 6: Inferential logistic regression

Goal: estimate associations between customer characteristics and churn while keeping the analysis interpretable.

This stage uses statsmodels logistic regression and includes:

- categorical encoding with chosen reference categories
- review of multicollinearity risk
- coefficient interpretation
- odds ratios and confidence intervals
- explanation of associations rather than causal claims

This is a strong interview topic because it combines statistical reasoning, modeling, and business interpretation.

### Stage 7: Predictive modeling

Goal: compare models that can distinguish churned and retained customers.

Common modeling approach:

- logistic regression as the interpretable baseline
- random forest as a more flexible model
- cross-validation
- class imbalance handling
- evaluation on recall, precision, F1, PR-AUC, ROC-AUC, and confusion matrix

The project intentionally avoids relying on accuracy alone because churn is imbalanced and precision/recall matter more in practice.

### Stage 8: Business recommendations and experiment design

Goal: translate analysis findings into actions and propose testable interventions.

Examples of business recommendations could include:

- targeted retention outreach for customers in month-to-month contracts
- interventions for fiber optic customers with high churn risk
- lifecycle outreach for new customers in shorter tenure segments
- retention offers for high-value customers at risk of churn

Each recommendation is framed as a hypothesis to test, not a guaranteed result. The project emphasizes designing experiments instead of claiming causal proof.

---

## 5. Why we did these things

This project was designed to teach and demonstrate a realistic, end-to-end data science workflow. The key reasons were:

- to validate data before any modeling
- to avoid making false claims from raw data
- to keep a clear record of what changed in the dataset
- to answer real business questions with evidence
- to apply both descriptive and inferential statistics
- to separate assoications from causation
- to prepare for interviews with method-aware explanations

This is more valuable than just building a model because it shows a mature analytical process.

---

## 6. Important project principles

These are the key principles that guide the project:

- Never fabricate results.
- Save outputs to project report folders so numbers are traceable.
- Run code before writing interpretation.
- Use observational language, not causal language.
- Use effect sizes and business context, not just p-values.
- Keep transformations transparent and documented.
- Maintain reproducibility with a fixed random state and relative project paths.

These rules are especially important for portfolio and interview work.

---

## 7. Resume-ready language

### Resume bullet set 1

- Built and validated a churn analysis workflow for a 7,043-row Telco dataset, including schema checks, duplicate validation, category verification, and logic integrity checks.
- Created a reproducible Python and SQL pipeline to summarize churn across contract type, service type, payment method, and tenure segment.
- Identified high-risk churn groups from the data, including month-to-month customers and fiber optic users, with traceable analysis outputs saved for review.

### Resume bullet set 2

- Designed a data-cleaning and transformation workflow with logged changes for missing bill values, feature type conversion, and churn target creation.
- Performed exploratory customer churn analysis using SQLite and Python, surfacing business-relevant retention patterns for reporting and decision support.
- Emphasized statistics-first analysis, maintaining clear separation between association and causation while documenting all assumptions and limitations.

### Resume bullet set 3

- Developed a structured customer retention analysis project covering data validation, cleaning, exploratory analysis, statistical inference, and modeling considerations.
- Converted raw customer data into a reproducible analytical dataset and generated project reports for transparency, review, and stakeholder communication.
- Presented churn risk patterns and retention signals in a business-friendly way, supporting downstream analytical and experimental work.

---

## 8. Key project findings

These are the strongest findings from the verified outputs:

- Overall churn rate is 26.54%.
- Month-to-month customers have a churn rate of 42.71%.
- Two-year contract customers have a churn rate of 2.83%.
- Fiber optic customers have a churn rate of 41.89%.
- Customers with no internet service have a churn rate of 7.40%.
- Customers in the 0 to 12 month tenure segment have a churn rate of 47.44%.
- Customers in the 49+ month tenure segment have a churn rate of 9.51%.

These are the kinds of findings that are useful for interviews, stakeholder conversations, and retention strategy discussions.

---

## 9. How to talk about this in an interview

A strong interview answer is:

"I built a customer churn analysis project using the IBM Telco dataset. The work included validating the raw data, fixing a structural issue in TotalCharges, cleaning the dataset, and then exploring churn patterns by contract type, service, tenure, and payment method. I used SQL and Python to surface business-relevant patterns and kept a traceable record of all outputs. The key takeaway was that churn was much higher among month-to-month customers and fiber optic users, which suggests the data supports follow-up retention analysis and experiment design. The project emphasized reproducibility, evidence-based interpretation, and careful language around observational data."

---

## 10. What we have completed so far

Completed:

- project scaffold
- raw data validation
- cleaning workflow
- transformation log
- SQL analysis and EDA outputs
- saved reports and figures
- project documentation

Next likely stages:

- statistical tests
- bootstrap and permutation work
- inferential logistic regression
- predictive modeling comparison
- experiment design
- executive summary and interview guide refinement

---

## 11. Final takeaway

This project is strong because it shows the full analytical process, not just a model. It demonstrates that you can work from messy raw data to clean, reproducible, business-relevant analysis, while staying rigorous about assumptions, uncertainty, and interpretation. That is exactly the kind of thinking employers value in data science and analytics work.
