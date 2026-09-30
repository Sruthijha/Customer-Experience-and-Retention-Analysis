# Customer Experience and Retention Analysis

This project analyzes IBM Telco Customer Churn data to study customer retention, churn patterns, and predictive risk factors. It follows a statistical and analytical workflow instead of a pure classifier-only approach.

## Business question

Which customer characteristics and service patterns are associated with churn, and how can that information guide retention strategy and future experiments?

## Dataset

The analysis uses the IBM telco churn sample dataset, saved in the repo at `data/raw/telco_customer_churn_raw.csv`.

## Repo structure

- `data/raw/` contains the raw CSV source.
- `data/processed/` stores cleaned data outputs.
- `src/` stores reusable Python logic.
- `sql/` stores analysis queries.
- `notebooks/` stores staged analysis notebooks.
- `reports/` stores figures and summaries.

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
