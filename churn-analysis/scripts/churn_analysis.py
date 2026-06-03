import pandas as pd

# Load dataset
df = pd.read_csv("data/telco.csv")

# Basic info
print("Total Customers:", len(df))

# Churn rate
churn_rate = (df['Churn'] == 'Yes').mean()
print("Churn Rate:", round(churn_rate * 100, 2), "%")

# Churn by contract type
churn_by_contract = df.groupby('Contract')['Churn'].apply(lambda x: (x == 'Yes').mean())

print("\nChurn by Contract Type:")
print(churn_by_contract)
