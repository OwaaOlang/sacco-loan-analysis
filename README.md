# SACCO Loan Portfolio - Quarterly Repayment Rate

Question: What percentage of loans issued in each quarter are fully repaid within 90 days?

## Method
- Days to repay = repayment_date - issue_date
- Repaid in 90 days = Fully Repaid AND days_to_repay <= 90
- Repayment Rate = Repaid in 90 days / Total loans in quarter * 100

## Results
| Quarter | Total Loans | Repaid in 90 | Rate |
|---------|-------------|--------------|------|
| 2025Q1 | 50 | 24 | 48.0% |
| 2025Q2 | 50 | 24 | 48.0% |
| 2025Q3 | 50 | 23 | 46.0% |
| 2025Q4 | 50 | 23 | 46.0% |

## Recommendation
Introduce 30-day and 60-day reminders plus an early-repayment incentive, with extra focus on Q3/Q4 loans where the rate drops to 46%.

## Files
- sacco_loans.csv - sample data (200 loans)
- quarterly_repayment_rate.csv - results table
- sacco_quarterly_rate.png - chart
- sacco_analysis.py - analysis code