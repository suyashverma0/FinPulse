import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(r"C:\FinPulse")
INPUT_PATH = PROJECT_ROOT / "data" / "powerbi" / "FinPulse_PowerBI.csv"

CHART_FOLDER = PROJECT_ROOT / "python" / "charts"
TABLE_FOLDER = PROJECT_ROOT / "python" / "tables"

CHART_FOLDER.mkdir(parents=True, exist_ok=True)
TABLE_FOLDER.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_PATH)

df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
df["VALUE DATE"] = pd.to_datetime(df["VALUE DATE"], errors="coerce")

df["YEAR"] = df["DATE"].dt.year
df["MONTH"] = df["DATE"].dt.month

monthly_analysis = (
    df.groupby(["YEAR", "MONTH"])
    .agg(
        transactions=("DATE", "count"),
        deposits=("DEPOSIT AMT", "sum"),
        withdrawals=("WITHDRAWAL AMT", "sum"),
        net_cash_flow=("NET AMOUNT", "sum")
    )
    .reset_index()
)

monthly_analysis["MONTH DATE"] = pd.to_datetime(
    dict(
        year=monthly_analysis["YEAR"].astype(int),
        month=monthly_analysis["MONTH"].astype(int),
        day=1
    )
)


monthly_analysis = monthly_analysis.sort_values("MONTH DATE")

monthly_balance = (
    df.sort_values("DATE")
    .set_index("DATE")
    .resample("ME")["BALANCE AMT"]
    .last()
    .reset_index()
)

daily_activity = (
    df.groupby("DATE")
    .size()
    .reset_index(name="transaction_count")
)

plt = __import__("matplotlib.pyplot", fromlist=["plt"])

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_analysis["MONTH DATE"],
    monthly_analysis["deposits"],
    marker="o",
    label="Deposits"
)
plt.plot(
    monthly_analysis["MONTH DATE"],
    monthly_analysis["withdrawals"],
    marker="o",
    label="Withdrawals"
)
plt.title("Monthly Deposits vs Withdrawals")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(
    CHART_FOLDER / "monthly_deposits_vs_withdrawals.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

plt.figure(figsize=(12, 6))
plt.bar(
    monthly_analysis["MONTH DATE"],
    monthly_analysis["net_cash_flow"]
)
plt.axhline(0, linewidth=1)
plt.title("Monthly Net Cash Flow")
plt.xlabel("Month")
plt.ylabel("Net Cash Flow")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    CHART_FOLDER / "monthly_net_cashflow.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_balance["DATE"],
    monthly_balance["BALANCE AMT"],
    marker="o"
)
plt.title("Monthly Ending Balance Trend")
plt.xlabel("Month")
plt.ylabel("Balance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    CHART_FOLDER / "balance_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

plt.figure(figsize=(12, 6))
plt.plot(
    daily_activity["DATE"],
    daily_activity["transaction_count"]
)
plt.title("Daily Transaction Activity")
plt.xlabel("Date")
plt.ylabel("Transaction Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    CHART_FOLDER / "daily_transaction_activity.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

monthly_analysis.to_csv(
    TABLE_FOLDER / "monthly_analysis.csv",
    index=False
)

daily_activity.to_csv(
    TABLE_FOLDER / "daily_transaction_activity.csv",
    index=False
)

monthly_balance.to_csv(
    TABLE_FOLDER / "monthly_balance.csv",
    index=False
)

print("Cash flow analysis completed successfully.")
print(f"Monthly records: {len(monthly_analysis)}")
print(f"Daily records: {len(daily_activity)}")
print(f"Monthly balance records: {len(monthly_balance)}")