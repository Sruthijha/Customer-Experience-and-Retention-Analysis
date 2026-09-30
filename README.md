# Customer Experience and Retention Analysis

A customer churn and retention analysis project using IBM Telco sample data, with a focus on validation, SQL exploration, statistical thinking, and business-ready interpretation.

## Project goal

This project studies which customer attributes and service patterns are associated with churn, and how those patterns can inform retention strategy and future business experiments.

## Why this project matters

Customer retention is a critical business problem for subscription-based services. This analysis is designed to show how a data-science workflow can move from raw data quality checks to exploratory analysis, statistical inference, and decision support.

## Dataset

The project uses the IBM Telco Customer Churn sample dataset, a fictional telco dataset used for churn analysis.

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
├── LICENSE
└── .github/
```

## Main files to review first

- `notebooks/01_data_validation.ipynb` for the validation workflow
- `notebooks/02_eda_sql.ipynb` for SQL and EDA output
- `src/data_processing.py` for the cleaning and transformation logic
- `reports/project_reference.md` for the full project narrative and resume-ready summary
- `reports/results/overall_summary.csv` for verified dataset summaries

## Verified findings

From the saved project outputs, the current dataset shows:

- Overall churn rate: 26.54%
- Month-to-month churn: 42.71%
- One-year contract churn: 11.27%
- Two-year contract churn: 2.83%
- Fiber optic churn: 41.89%
- No internet service churn: 7.40%
- 0 to 12 month tenure churn: 47.44%

These figures are saved in the project output files and are intended for business interpretation and follow-up analysis.

## Workflow

This project follows a practical data-science pipeline:

1. Validate the raw dataset
2. Document structure and quality issues
3. Clean and transform the data with traceability
4. Explore churn patterns with SQL and descriptive analysis
5. Run inferential and resampling-based statistical checks
6. Prepare for modeling and experiment design
7. Translate findings into business recommendations

## Reproduction

1. Create and activate a Python environment.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the validation and cleaning workflow:
   `python src/data_processing.py`
4. Run the SQL analysis workflow:
   `python src/sql_analysis.py`
5. Open the notebooks in order to explore the analysis in detail.

## Notes

This project uses observational data and focuses on association rather than causation. The goal is to identify patterns, quantify uncertainty, and support business decisions with evidence while staying careful about statistical interpretation.
