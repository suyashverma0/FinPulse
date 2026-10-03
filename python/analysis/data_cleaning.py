import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(r"C:\FinPulse")

INPUT_PATH = PROJECT_ROOT / "data" / "process" / "new one.csv"

OUTPUT_FOLDER = PROJECT_ROOT / "data" / "powerbi"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

OUTPUT_PATH = OUTPUT_FOLDER / "FinPulse_PowerBI.csv"


print("Loading dataset...")

df = pd.read_csv(INPUT_PATH)

print(f"Original shape: {df.shape}")


df.columns = [
    col.strip()
    for col in df.columns
]



df = df.dropna(axis=1, how="all")



df["DATE"] = pd.to_datetime(
    df["DATE"],
    errors="coerce"
)

df["VALUE DATE"] = pd.to_datetime(
    df["VALUE DATE"],
    errors="coerce"
)

amount_columns = [
    "WITHDRAWAL AMT",
    "DEPOSIT AMT",
    "BALANCE AMT"
]

for column in amount_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )



df["WITHDRAWAL AMT"] = (
    df["WITHDRAWAL AMT"]
    .fillna(0)
)

df["DEPOSIT AMT"] = (
    df["DEPOSIT AMT"]
    .fillna(0)
)



df["TRANSACTION DETAILS"] = (
    df["TRANSACTION DETAILS"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
)


df["Account No"] = (
    df["Account No"]
    .fillna(0)
)


duplicate_count = df.duplicated().sum()

print(f"Duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    df = df.drop_duplicates()


df["TRANSACTION TYPE"] = np.select(
    [
        df["DEPOSIT AMT"] > 0,
        df["WITHDRAWAL AMT"] > 0
    ],
    [
        "Deposit",
        "Withdrawal"
    ],
    default="Other"
)


df["NET AMOUNT"] = (
    df["DEPOSIT AMT"]
    - df["WITHDRAWAL AMT"]
)


df["TRANSACTION VALUE"] = (
    df["DEPOSIT AMT"]
    + df["WITHDRAWAL AMT"]
)


df["YEAR"] = df["DATE"].dt.year

df["MONTH"] = df["DATE"].dt.month

df["MONTH NAME"] = (
    df["DATE"]
    .dt.month_name()
)

df["DAY"] = df["DATE"].dt.day

df["DAY NAME"] = (
    df["DATE"]
    .dt.day_name()
)

df["WEEKDAY"] = (
    df["DATE"]
    .dt.dayofweek
)


transaction_value_threshold = (
    df["TRANSACTION VALUE"]
    .quantile(0.99)
)

df["HIGH VALUE FLAG"] = np.where(
    df["TRANSACTION VALUE"] >= transaction_value_threshold,
    "High Value",
    "Normal"
)



df = df.sort_values(
    by=["DATE", "VALUE DATE"],
    na_position="last"
)


print("\nFinal dataset information:")
print("--------------------------------")

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Accounts: {df['Account No'].nunique()}")
print(f"Date range: {df['DATE'].min()} → {df['DATE'].max()}")

print("\nTransaction types:")
print(df["TRANSACTION TYPE"].value_counts())

#  SAVE POWER BI DATASET


df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

print("\n--------------------------------")
print("Cleaning completed successfully.")
print(f"Power BI file saved at:")
print(OUTPUT_PATH)
print("--------------------------------")