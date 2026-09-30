from __future__ import annotations

import sqlite3
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEAN_CSV = PROJECT_ROOT / "data" / "processed" / "telco_customer_churn_clean.csv"
DB_PATH = PROJECT_ROOT / "data" / "processed" / "telco_customer_churn_clean.db"
RESULTS_DIR = PROJECT_ROOT / "reports" / "results"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"


def load_clean_data() -> pd.DataFrame:
    df = pd.read_csv(CLEAN_CSV)
    if "churn_flag" not in df.columns:
        raise ValueError("Cleaned dataset is missing churn_flag.")
    return df


def create_sqlite_database(df: pd.DataFrame) -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("customer_churn", conn, index=False, if_exists="replace")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_customer_churn_contract ON customer_churn(Contract)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_customer_churn_churn_flag ON customer_churn(churn_flag)")
    return conn


def run_query(conn: sqlite3.Connection, sql: str) -> pd.DataFrame:
    return pd.read_sql_query(sql, conn)


def save_results() -> dict[str, pd.DataFrame]:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = load_clean_data()
    conn = create_sqlite_database(df)

    overall_sql = """
        SELECT
            COUNT(*) AS customer_count,
            ROUND(AVG(churn_flag), 4) AS churn_rate,
            ROUND(AVG(tenure), 2) AS avg_tenure,
            ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
        FROM customer_churn
    """
    contract_sql = """
        SELECT
            Contract,
            COUNT(*) AS customer_count,
            ROUND(AVG(churn_flag) * 100, 2) AS churn_rate_pct,
            ROUND(AVG(tenure), 2) AS avg_tenure,
            ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
        FROM customer_churn
        GROUP BY Contract
        ORDER BY churn_rate_pct DESC
    """
    payment_sql = """
        SELECT
            PaymentMethod,
            COUNT(*) AS customer_count,
            ROUND(AVG(churn_flag) * 100, 2) AS churn_rate_pct,
            ROUND(AVG(tenure), 2) AS avg_tenure,
            ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
        FROM customer_churn
        GROUP BY PaymentMethod
        ORDER BY churn_rate_pct DESC
    """
    internet_sql = """
        SELECT
            InternetService,
            COUNT(*) AS customer_count,
            ROUND(AVG(churn_flag) * 100, 2) AS churn_rate_pct,
            ROUND(AVG(tenure), 2) AS avg_tenure,
            ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
        FROM customer_churn
        GROUP BY InternetService
        ORDER BY churn_rate_pct DESC
    """
    tenure_sql = """
        SELECT
            CASE
                WHEN tenure <= 12 THEN '0-12'
                WHEN tenure <= 24 THEN '13-24'
                WHEN tenure <= 36 THEN '25-36'
                WHEN tenure <= 48 THEN '37-48'
                ELSE '49+'
            END AS tenure_segment,
            COUNT(*) AS customer_count,
            ROUND(AVG(churn_flag) * 100, 2) AS churn_rate_pct,
            ROUND(AVG(tenure), 2) AS avg_tenure
        FROM customer_churn
        GROUP BY tenure_segment
        ORDER BY CASE tenure_segment
            WHEN '0-12' THEN 1
            WHEN '13-24' THEN 2
            WHEN '25-36' THEN 3
            WHEN '37-48' THEN 4
            ELSE 5
        END
    """

    results = {
        "overall_summary": run_query(conn, overall_sql),
        "contract_summary": run_query(conn, contract_sql),
        "payment_summary": run_query(conn, payment_sql),
        "internet_service_summary": run_query(conn, internet_sql),
        "tenure_segment_summary": run_query(conn, tenure_sql),
    }

    for name, data_frame in results.items():
        data_frame.to_csv(RESULTS_DIR / f"{name}.csv", index=False)

    contract_chart = results["contract_summary"].copy()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(contract_chart["Contract"], contract_chart["churn_rate_pct"], color="#1f77b4")
    ax.set_title("Churn rate by contract type")
    ax.set_xlabel("Contract")
    ax.set_ylabel("Churn rate (%)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "churn_by_contract.png", dpi=200)
    plt.close(fig)

    tenure_chart = results["tenure_segment_summary"].copy()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(tenure_chart["tenure_segment"], tenure_chart["customer_count"], color="#2ca02c")
    ax.set_title("Customer count by tenure segment")
    ax.set_xlabel("Tenure segment")
    ax.set_ylabel("Customer count")
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "tenure_distribution.png", dpi=200)
    plt.close(fig)

    conn.close()
    return results


if __name__ == "__main__":
    summary = save_results()
    print(summary["overall_summary"].to_dict(orient="records"))
    print("Saved SQL analysis outputs to reports/results and figures to reports/figures.")
