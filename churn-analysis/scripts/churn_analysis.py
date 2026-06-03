import pandas as pd

# Load dataset
df = pd.read_csv("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Summary
print("Total Customers:", len(df))

# Churn rate
churn_rate = (df['Churn'] == 'Yes').mean()
print("Churn Rate:", f"{churn_rate:.2%}")

# Churn by contract
churn_by_contract = df.groupby('Contract')['Churn'].apply(
    lambda x: (x == 'Yes').mean()
)

print("\nChurn by Contract Type:\n")
for contract, value in churn_by_contract.items():
    print(f"{contract}: {value:.2%}")