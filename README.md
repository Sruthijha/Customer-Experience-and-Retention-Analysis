# Customer Experience and Retention Analysis

This project analyzes IBM Telco Customer Churn data to study customer retention, churn patterns, and predictive risk factors. It follows a statistical and analytical workflow instead of a pure classifier-only approach.

## Business question

Which customer characteristics and service patterns are associated with churn, and how can that information guide retention strategy and future experiments?

## Dataset

The analysis uses the IBM telco churn sample dataset, saved in the repo at `data/raw/telco_customer_churn_raw.csv`.

## Repo structure

The project is organized so the most important folders are visible immediately from the repository home page:

```text
customer-retention-statistics/
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
└── CLAUDE.md
```

## Quick access to the main files

- Data source: `data/raw/telco_customer_churn_raw.csv`
- Cleaned dataset: `data/processed/telco_customer_churn_clean.csv`
- Validation notebook: `notebooks/01_data_validation.ipynb`
- SQL and EDA notebook: `notebooks/02_eda_sql.ipynb`
- Statistical inference notebook: `notebooks/03_statistical_inference.ipynb`
- Modeling notebook: `notebooks/04_modeling.ipynb`
- Data processing logic: `src/data_processing.py`
- SQL analysis logic: `src/sql_analysis.py`
- Results folder: `reports/results/`
- Project reference: `reports/project_reference.md`

## Reproduction

1. Create a Python environment.
2. Install requirements:
   `pip install -r requirements.txt`
3. Download the raw data into `data/raw/`.
4. Run the validation and cleaning workflow from `src/data_processing.py`.
5. Open notebooks in order from `notebooks/`.

## Current stage

The project is set up for Stage 1 validation and Stage 2 cleaning, with data processing code and saved outputs based on the real IBM telco dataset.

## Notes

This is observational data. The project focuses on associations and statistical inference, not causal claims.
