import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("creditcard_2023.csv")

# Check data
print(df.head())
print(df.info())

# Check fraud count
print("\nFraud vs Normal Transactions:")
print(df['Class'].value_counts())

# Plot fraud vs normal
df['Class'].value_counts().plot(kind='bar')

plt.title("Fraud vs Normal Transactions")
plt.xlabel("0 = Normal, 1 = Fraud")
plt.ylabel("Count")
plt.show()

# Amount distribution
plt.hist(df['Amount'], bins=50)

plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Count")
plt.show()