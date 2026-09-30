from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

RANDOM_STATE = 42

RAW_DATA_PATH = Path("data/raw/telco_customer_churn_raw.csv")
CLEAN_DATA_PATH = Path("data/processed/telco_customer_churn_clean.csv")
RAW_VALIDATION_PATH = Path("reports/validation_summary_raw.csv")
CLEAN_VALIDATION_PATH = Path("reports/validation_summary_clean.csv")
TRANSFORMATION_LOG_PATH = Path("reports/transformation_log.csv")

REQUIRED_COLUMNS = [
    "customerID",
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges",
    "Churn",
]

ALLOWED_CATEGORIES = {
    "gender": ["Female", "Male"],
    "SeniorCitizen": ["0", "1"],
    "Partner": ["Yes", "No"],
    "Dependents": ["Yes", "No"],
    "PhoneService": ["Yes", "No"],
    "MultipleLines": ["No phone service", "No", "Yes"],
    "InternetService": ["DSL", "Fiber optic", "No"],
    "OnlineSecurity": ["No", "Yes", "No internet service"],
    "OnlineBackup": ["No", "Yes", "No internet service"],
    "DeviceProtection": ["No", "Yes", "No internet service"],
    "TechSupport": ["No", "Yes", "No internet service"],
    "StreamingTV": ["No", "Yes", "No internet service"],
    "StreamingMovies": ["No", "Yes", "No internet service"],
    "Contract": ["Month-to-month", "One year", "Two year"],
    "PaperlessBilling": ["Yes", "No"],
    "PaymentMethod": [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)",
    ],
    "Churn": ["Yes", "No"],
}


def load_raw(path: str | Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw CSV as text to preserve string values and blanks."""
    data_path = Path(path)
    df = pd.read_csv(data_path, dtype=str, keep_default_na=False)
    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {sorted(missing)}")
    return df


def validate_raw(df: pd.DataFrame) -> pd.DataFrame:
    """Return a simple summary table of raw validation checks."""
    rows = len(df)
    columns = df.shape[1]

    duplicate_rows = int(df.duplicated().sum())
    duplicate_customer_ids = int(df["customerID"].duplicated().sum())

    blank_total_charges = int(df["TotalCharges"].astype(str).str.strip().eq("").sum())
    tenure_zero_count = int(df["tenure"].astype(str).str.strip().eq("0").sum())

    total_charges_numeric = pd.to_numeric(df["TotalCharges"], errors="coerce")
    ratio = total_charges_numeric / (pd.to_numeric(df["tenure"], errors="coerce") * pd.to_numeric(df["MonthlyCharges"], errors="coerce"))
    ratio_outside = int(((ratio < 0.5) | (ratio > 1.5)).sum())
    ratio_missing = int(ratio.isna().sum())

    category_issues = []
    for column, allowed in ALLOWED_CATEGORIES.items():
        values = df[column].astype(str).str.strip()
        invalid = sorted(set(values) - set(str(v).strip() for v in allowed))
        if invalid:
            category_issues.append({"column": column, "invalid_values": "; ".join(invalid)})

    logic_issue_rows = []
    internet_service = df["InternetService"].astype(str).str.strip()
    online_security = df["OnlineSecurity"].astype(str).str.strip()
    online_backup = df["OnlineBackup"].astype(str).str.strip()
    device_protection = df["DeviceProtection"].astype(str).str.strip()
    tech_support = df["TechSupport"].astype(str).str.strip()
    streaming_tv = df["StreamingTV"].astype(str).str.strip()
    streaming_movies = df["StreamingMovies"].astype(str).str.strip()

    internet_addon_mismatch = (
        internet_service.eq("No")
        & (
            online_security.ne("No internet service")
            | online_backup.ne("No internet service")
            | device_protection.ne("No internet service")
            | tech_support.ne("No internet service")
            | streaming_tv.ne("No internet service")
            | streaming_movies.ne("No internet service")
        )
    )
    multiple_lines_mismatch = (
        df["PhoneService"].astype(str).str.strip().eq("No")
        & df["MultipleLines"].astype(str).str.strip().ne("No phone service")
    )

    logic_checks = {
        "InternetService_no_vs_addon": int(internet_addon_mismatch.sum()),
        "MultipleLines_no_phone_service": int(multiple_lines_mismatch.sum()),
    }

    summary = pd.DataFrame(
        [
            {"metric": "rows", "value": rows},
            {"metric": "columns", "value": columns},
            {"metric": "duplicate_rows", "value": duplicate_rows},
            {"metric": "duplicate_customerID", "value": duplicate_customer_ids},
            {"metric": "blank_TotalCharges", "value": blank_total_charges},
            {"metric": "tenure_zero_count", "value": tenure_zero_count},
            {"metric": "ratio_outside_0_5_to_1_5", "value": ratio_outside},
            {"metric": "ratio_missing", "value": ratio_missing},
            {"metric": "raw_churn_yes", "value": int(df["Churn"].astype(str).str.strip().eq("Yes").sum())},
            {"metric": "raw_churn_no", "value": int(df["Churn"].astype(str).str.strip().eq("No").sum())},
            {"metric": "logic_InternetService_no_vs_addon", "value": logic_checks["InternetService_no_vs_addon"]},
            {"metric": "logic_MultipleLines_no_phone_service", "value": logic_checks["MultipleLines_no_phone_service"]},
        ]
    )

    if category_issues:
        summary = pd.concat(
            [summary, pd.DataFrame(category_issues).rename(columns={"column": "metric", "invalid_values": "value"})],
            ignore_index=True,
        )

    return summary


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the raw telco dataset while preserving the original churn labels."""
    cleaned = df.copy()
    cleaned["TotalCharges"] = cleaned["TotalCharges"].astype(str).str.strip()
    blank_total_charges = cleaned["TotalCharges"].eq("")
    tenure_zero_mask = cleaned["tenure"].astype(str).str.strip().eq("0")
    if not bool(blank_total_charges.equals(tenure_zero_mask)):
        raise ValueError("Blank TotalCharges rows do not match tenure = 0 rows. Review the raw data before cleaning.")

    cleaned.loc[blank_total_charges, "TotalCharges"] = "0"

    cleaned["tenure"] = pd.to_numeric(cleaned["tenure"], errors="raise").astype(int)
    cleaned["MonthlyCharges"] = pd.to_numeric(cleaned["MonthlyCharges"], errors="raise").astype(float)
    cleaned["TotalCharges"] = pd.to_numeric(cleaned["TotalCharges"], errors="raise").astype(float)

    cleaned["SeniorCitizen"] = cleaned["SeniorCitizen"].map({"0": "No", "1": "Yes"})
    cleaned["churn_flag"] = cleaned["Churn"].str.strip().str.lower().eq("yes").astype(int)

    for column in ["customerID", "gender", "Partner", "Dependents", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "Churn"]:
        cleaned[column] = cleaned[column].astype(str).str.strip()

    return cleaned


def validate_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Validate the cleaned dataset and return a summary table."""
    summary = pd.DataFrame(
        [
            {"metric": "rows", "value": len(df)},
            {"metric": "columns", "value": df.shape[1]},
            {"metric": "duplicate_customerID", "value": int(df["customerID"].duplicated().sum())},
            {"metric": "missing_totalcharges", "value": int(df["TotalCharges"].isna().sum())},
            {"metric": "series_unique_tenure", "value": int(df["tenure"].nunique())},
            {"metric": "min_tenure", "value": int(df["tenure"].min())},
            {"metric": "max_tenure", "value": int(df["tenure"].max())},
            {"metric": "mean_monthly_charges", "value": float(df["MonthlyCharges"].mean())},
            {"metric": "mean_total_charges", "value": float(df["TotalCharges"].mean())},
            {"metric": "churn_yes", "value": int(df["churn_flag"].sum())},
            {"metric": "churn_no", "value": int((1 - df["churn_flag"]).sum())},
        ]
    )
    return summary


def save_outputs() -> None:
    """Run the validation and cleaning workflow and save all Stage 1 outputs."""
    raw_df = load_raw(RAW_DATA_PATH)
    raw_summary = validate_raw(raw_df)
    RAW_VALIDATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    raw_summary.to_csv(RAW_VALIDATION_PATH, index=False)

    clean_df = clean(raw_df)
    clean_summary = validate_clean(clean_df)

    CLEAN_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    clean_df.to_csv(CLEAN_DATA_PATH, index=False)
    clean_summary.to_csv(CLEAN_VALIDATION_PATH, index=False)

    transformation_log = pd.DataFrame(
        [
            {
                "step": "load_raw",
                "action": "Read CSV with dtype=str and keep_default_na=False to retain blank strings.",
                "reason": "Preserve raw text values so we can validate blanks and categories before conversion.",
            },
            {
                "step": "blank_totalcharges_fill",
                "action": "Filled blank TotalCharges with 0 for tenure = 0 customers only.",
                "reason": "These customers were not billed yet, so the missing value is structurally zero rather than unknown.",
            },
            {
                "step": "coerce_numeric_types",
                "action": "Converted tenure, MonthlyCharges, and TotalCharges to numeric types.",
                "reason": "Support modeling and summary statistics.",
            },
            {
                "step": "seniorcitizen_recode",
                "action": "Converted SeniorCitizen 0/1 to No/Yes.",
                "reason": "Keep categorical encoding consistent with the rest of the dataset.",
            },
            {
                "step": "churn_flag_addition",
                "action": "Added churn_flag equal to 1 when Churn equals Yes.",
                "reason": "Provide a binary target for downstream modeling.",
            },
        ]
    )
    transformation_log.to_csv(TRANSFORMATION_LOG_PATH, index=False)


if __name__ == "__main__":
    save_outputs()
    print(f"Raw validation summary saved to {RAW_VALIDATION_PATH}")
    print(f"Clean data saved to {CLEAN_DATA_PATH}")
    print(f"Clean validation summary saved to {CLEAN_VALIDATION_PATH}")
    print(f"Transformation log saved to {TRANSFORMATION_LOG_PATH}")
