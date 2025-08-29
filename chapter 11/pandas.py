import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 28],
    "Salary": [50000, 60000, 75000, 80000, 65000]
}

df = pd.DataFrame(data)

# Show the DataFrame
print("Full DataFrame:")
print(df)

# Get basic info
print("\nSummary statistics:")
print(df.describe())

# Select one column
print("\nNames only:")
print(df["Name"])

# Filter rows (Age > 30)
print("\nPeople older than 30:")
print(df[df["Age"] > 30])

# Calculate average salary
avg_salary = df["Salary"].mean()
print(f"\nAverage Salary: {avg_salary}")
