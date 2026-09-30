# Customer Experience and Retention Analysis

A customer churn and retention analysis project built around IBM Telco sample data, with a statistics-first workflow, validation checks, SQL analysis, and modeling preparation.

## Overview

This project studies which customer characteristics and service patterns are associated with churn. The work focuses on data quality, exploratory analysis, statistical inference, and business interpretation instead of only model output.

## Business question

Which customer attributes and service patterns are associated with churn, and how can that understanding support retention strategies and future experiments?

## Dataset

This project uses the IBM Telco Customer Churn sample dataset, which is a fictional telco dataset used for churn analysis.

Key files:

- Raw data: `data/raw/telco_customer_churn_raw.csv`
- Cleaned data: `data/processed/telco_customer_churn_clean.csv`

## Project structure

```text
Customer-Experience-and-Retention-Analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   └── telco_customer_churn_raw.csv
│   └── processed/
│       └── telco_customer_churn_clean.csv
├── notebooks/
│   ├── 01_data_validation.ipynb
│   ├── 02_eda_sql.ipynb
│   ├── 03_statistical_inference.ipynb
│   └── 04_modeling.ipynb
├── src/
│   ├── data_processing.py
│   ├── sql_analysis.py
│   ├── statistical_tests.py
│   ├── modeling.py
│   └── __init__.py
├── sql/
│   └── customer_analysis.sql
├── reports/
│   ├── figures/
│   │   ├── churn_by_contract.png
│   │   └── tenure_distribution.png
│   ├── results/
│   │   ├── overall_summary.csv
│   │   ├── contract_summary.csv
│   │   ├── payment_summary.csv
│   │   ├── internet_service_summary.csv
│   │   └── tenure_segment_summary.csv
│   ├── validation_summary_raw.csv
│   ├── validation_summary_clean.csv
│   ├── transformation_log.csv
│   ├── executive_summary.md
│   ├── interview_guide.md
│   └── project_reference.md
├── CLAUDE.md
└── LICENSE
```

## Key files to open first

- `notebooks/01_data_validation.ipynb` for the validation workflow
- `notebooks/02_eda_sql.ipynb` for the SQL and EDA stage
- `src/data_processing.py` for the cleaning workflow
- `reports/project_reference.md` for the full project narrative and resume-ready summary
- `reports/results/overall_summary.csv` for the verified summary metrics

## Verified results from the current data

From the saved project outputs, the analysis shows:

- Overall churn rate: 26.54%
- Month-to-month churn: 42.71%
- One-year contract churn: 11.27%
- Two-year contract churn: 2.83%
- Fiber optic churn: 41.89%
- No internet service churn: 7.40%
- Customers in 0 to 12 months tenure: 47.44% churn

These figures come from project outputs saved under `reports/results/` and are intended to support business interpretation and future model work.

## Methodology

The workflow includes:

1. Data validation and documentation of data issues
2. Data cleaning and transformation logging
3. SQL-based customer segmentation and churn summaries
4. Statistical tests and effect-size thinking
5. Modeling preparation and comparison of predictive approaches
6. Business recommendations and experiment design

## Reproduction

1. Create and activate a Python environment.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the validation and cleaning workflow:
   `python src/data_processing.py`
4. Run the SQL and EDA workflow:
   `python src/sql_analysis.py`
5. Open the notebooks in order for the full analysis workflow.

## Notes

This project uses observational data and focuses on association rather than causation. The analysis is intended to support retention strategy and data-science interview preparation, not to claim causal conclusions.
