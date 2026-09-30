WITH churn_summary AS (
    SELECT
        Contract,
        COUNT(*) AS customer_count,
        AVG(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0.0 END) AS churn_rate,
        AVG(tenure) AS avg_tenure,
        AVG(MonthlyCharges) AS avg_monthly_charges
    FROM telco_customer_churn_clean
    GROUP BY Contract
)
SELECT
    Contract,
    customer_count,
    ROUND(churn_rate * 100, 2) AS churn_rate_pct,
    ROUND(avg_tenure, 2) AS avg_tenure,
    ROUND(avg_monthly_charges, 2) AS avg_monthly_charges
FROM churn_summary
ORDER BY churn_rate DESC;
