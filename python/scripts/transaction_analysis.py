import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(r"C:\FinPulse")
INPUT_PATH = PROJECT_ROOT / "data" / "powerbi" / "FinPulse_PowerBI.csv"
OUTPUT_FOLDER = PROJECT_ROOT / "python" / "charts"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_PATH)

df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
df["VALUE DATE"] = pd.to_datetime(df["VALUE DATE"], errors="coerce")

transaction_summary = (
    df.groupby("TRANSACTION TYPE")
    .agg(
        transaction_count=("TRANSACTION TYPE", "count"),
        total_deposit=("DEPOSIT AMT", "sum"),
        total_withdrawal=("WITHDRAWAL AMT", "sum"),
        net_cash_flow=("NET AMOUNT", "sum"),
        average_transaction_value=("TRANSACTION VALUE", "mean")
    )
    .reset_index()
)

transaction_summary["percentage"] = (
    transaction_summary["transaction_count"]
    / transaction_summary["transaction_count"].sum()
    * 100
)

top_deposits = (
    df.nlargest(10, "DEPOSIT AMT")
    [
        [
            "DATE",
            "Account No",
            "TRANSACTION DETAILS",
            "DEPOSIT AMT",
            "BALANCE AMT"
        ]
    ]
)

top_withdrawals = (
    df.nlargest(10, "WITHDRAWAL AMT")
    [
        [
            "DATE",
            "Account No",
            "TRANSACTION DETAILS",
            "WITHDRAWAL AMT",
            "BALANCE AMT"
        ]
    ]
)

top_transaction_details = (
    df["TRANSACTION DETAILS"]
    .value_counts()
    .head(20)
    .reset_index()
)

top_transaction_details.columns = [
    "TRANSACTION DETAILS",
    "TRANSACTION COUNT"
]

high_value_transactions = (
    df.nlargest(100, "TRANSACTION VALUE")
    [
        [
            "DATE",
            "Account No",
            "TRANSACTION DETAILS",
            "TRANSACTION TYPE",
            "TRANSACTION VALUE",
            "NET AMOUNT",
            "BALANCE AMT"
        ]
    ]
)

account_summary = (
    df.groupby("Account No")
    .agg(
        transaction_count=("Account No", "count"),
        total_deposits=("DEPOSIT AMT", "sum"),
        total_withdrawals=("WITHDRAWAL AMT", "sum"),
        net_cash_flow=("NET AMOUNT", "sum"),
        average_balance=("BALANCE AMT", "mean")
    )
    .reset_index()
)

transaction_summary.to_csv(
    OUTPUT_FOLDER / "transaction_summary.csv",
    index=False
)

top_deposits.to_csv(
    OUTPUT_FOLDER / "top_10_deposits.csv",
    index=False
)

top_withdrawals.to_csv(
    OUTPUT_FOLDER / "top_10_withdrawals.csv",
    index=False
)

top_transaction_details.to_csv(
    OUTPUT_FOLDER / "top_transaction_descriptions.csv",
    index=False
)

high_value_transactions.to_csv(
    OUTPUT_FOLDER / "high_value_transactions.csv",
    index=False
)

account_summary.to_csv(
    OUTPUT_FOLDER / "account_summary.csv",
    index=False
)

print("Transaction analysis completed successfully.")
print(f"Transaction summary: {len(transaction_summary)} rows")
print(f"Top deposits: {len(top_deposits)} rows")
print(f"Top withdrawals: {len(top_withdrawals)} rows")
print(f"High-value transactions: {len(high_value_transactions)} rows")
print(f"Accounts analyzed: {len(account_summary)}")