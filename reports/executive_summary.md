# Executive Summary

This project studies IBM telco customer churn using observational data. The first stage focuses on validation and cleaning, with the goal of confirming the schema, blanks, and business rules before analysis.

The raw data has 7,043 rows and 21 columns. The main structural issue is 11 blank TotalCharges values, and those rows are exactly the customers with tenure equal to 0. The clean workflow fills those values with 0 and keeps the original churn labels for downstream work.

The next stages will compare churned and retained customers, run statistical tests, and build predictive models. The project keeps a clear separation between statistical association and causal language.
