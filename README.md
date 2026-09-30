# FinPulse 💰

### Bank Transaction & Financial Analytics

FinPulse is a financial data analytics project that turns raw banking transaction records into meaningful insights using **Python** and **Power BI**.

It focuses on transaction behavior, deposits, withdrawals, cash flow, transaction values, and balance trends, all explored through an interactive dashboard.

---

## 📌 About the Project

Raw transaction data holds valuable information about how money moves through accounts, but it is hard to understand as-is.

FinPulse cleans and analyzes this data in Python, then presents the results in an interactive Power BI dashboard.

```text
Raw Banking Data
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
Exploratory Data Analysis
       ↓
Financial & Transaction Analysis
       ↓
Power BI Dashboard
       ↓
Interactive Financial Insights
```

---

## 🔄 How FinPulse Works

| Step | Stage | Description |
|------|-------|-------------|
| 1 | **Raw Data** | Banking transactions with Account, Date, Transaction Details, Cheque Number, Value Date, Withdrawal Amount, Deposit Amount, and Balance Amount |
| 2 | **Data Cleaning** | Python cleans and standardizes the dataset |
| 3 | **Feature Engineering** | New fields are created: Transaction Type, Net Amount, Transaction Value, Year, Month, Day, Weekday |
| 4 | **Data Analysis** | Transactions, deposits, withdrawals, cash flow, balance, transaction values, and time trends are analyzed |
| 5 | **Power BI** | The processed dataset is imported to build interactive KPIs, charts, and filters |
| 6 | **Insights** | The dashboard lets users explore financial and transaction patterns interactively |

---

## 📷 Dashboard Preview

### Financial Overview
![Financial Overview](screenshots/dashboard_overview.png)

### Transaction Intelligence
![Transaction Intelligence](screenshots/transaction_intelligence.png)

---

## 📂 Project Structure

```text
FinPulse/
│
├── data/
│   ├── raw/
│   │   └── bank_original.csv
│   └── process/
│       └── new one.csv
│
├── python/
│   ├── notebooks/
│   │   └── FinPulse_EDA.ipynb
│   ├── scripts/
│   │   ├── data_cleaning.py
│   │   ├── transaction_analysis.py
│   │   └── cashflow_analysis.py
│   └── charts/
│       ├── transaction_distribution.png
│       ├── monthly_cashflow.png
│       ├── deposit_withdrawal_trend.png
│       ├── balance_trend.png
│       ├── transaction_type.png
│       └── daily_activity.png
│
├── powerbi/
│   └── FinPulse_Dashboard.pbix
│
├── screenshots/
│   ├── dashboard_overview.png
│   └── transaction_intelligence.png
│
├── reports/
│   └── business_insights.md
│
├── README.md
├── requirements.txt
└── LICENSE
```

| Folder / File | Purpose |
|---------------|---------|
| `data/raw/` | Original raw banking dataset |
| `data/process/` | Cleaned dataset used for analysis |
| `python/notebooks/` | Main EDA and analysis notebook |
| `python/scripts/` | Reusable Python scripts |
| `python/charts/` | Charts generated during Python analysis |
| `powerbi/` | Final Power BI dashboard |
| `screenshots/` | Dashboard screenshots |
| `reports/` | Business insights from the project |
| `README.md` | Project documentation |
| `requirements.txt` | Python dependencies |
| `LICENSE` | Project license |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/suyashverma0/FinPulse.git
cd FinPulse
```

Create and activate a virtual environment:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

1. Open the main notebook: `python/notebooks/FinPulse_EDA.ipynb`
2. Run it to perform the full workflow:

```text
Data Loading → Data Cleaning → Feature Engineering → EDA → Financial Analysis → Visualization
```

3. Use the processed dataset in `powerbi/FinPulse_Dashboard.pbix` to explore the interactive dashboard.

---

## 📊 Dataset

The project uses a **synthetic banking transaction dataset** with approximately **116K+ records**, including deposits, withdrawals, balances, dates, and transaction descriptions.

The dataset is used for educational and analytical purposes only.

---

## 🚀 Project Highlights

- Processed 116K+ banking transactions
- Built a complete Python data analytics workflow
- Performed data cleaning and feature engineering
- Analyzed transaction behavior, deposits, and withdrawals
- Calculated net cash flow and studied transaction value patterns
- Created time-based financial analysis
- Built an interactive Power BI dashboard with separate **Financial Overview** and **Transaction Intelligence** pages
- Used interactive filters for financial exploration

---

## 👨‍💻 Author

**Suyash Verma**
BCA — Data Science & AI

Interested in: Data Analytics · Data Science · Machine Learning · Business Intelligence

---

⭐ If you find this project useful, consider giving the repository a star.