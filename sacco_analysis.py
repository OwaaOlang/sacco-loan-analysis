import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sacco_loans.csv")
df['issue_date'] = pd.to_datetime(df['issue_date'])
df['repayment_date'] = pd.to_datetime(df['repayment_date'])

# Quarter from issue date
df['quarter'] = df['issue_date'].dt.to_period('Q').astype(str)

# Days to repay
df['days_to_repay'] = (df['repayment_date'] - df['issue_date']).dt.days

# Fully repaid within 90 days?
df['repaid_in_90'] = (df['repayment_status'] == 'Fully Repaid') & (df['days_to_repay'] <= 90)

# Quarterly table
table = df.groupby('quarter').agg(
    total_loans=('loan_id', 'count'),
    repaid_in_90=('repaid_in_90', 'sum')
).reset_index()

table['repayment_rate_%'] = round(table['repaid_in_90'] / table['total_loans'] * 100, 1)

print(table)
table.to_csv("quarterly_repayment_rate.csv", index=False)

# Chart
plt.figure(figsize=(8, 5))
plt.bar(table['quarter'], table['repayment_rate_%'])
plt.ylabel('Repaid within 90 days (%)')
plt.title('SACCO Quarterly Repayment Rate (within 90 days)')
plt.ylim(0, 100)
for i, v in enumerate(table['repayment_rate_%']):
    plt.text(i, v + 2, f"{v}%", ha='center')
plt.savefig("sacco_quarterly_rate.png")
plt.close()
print("Saved: quarterly_repayment_rate.csv and sacco_quarterly_rate.png")
