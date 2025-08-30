import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Name": ["Amit", "Ravi", "Sneha", "Priya"],
    "Age": [23, 25, 22, 28],
    "City": ["Delhi", "Mumbai", "Pune", "Bangalore"]
}

df = pd.DataFrame(data)

# Show the DataFrame
print("Full DataFrame:\n", df)

# Show first 2 rows
print("\nFirst 2 rows:\n", df.head(2))

# Select a single column
print("\nNames:\n", df["Name"])

# Filter rows where Age > 23
print("\nPeople older than 23:\n", df[df["Age"] > 23])

# Add a new column
df["Age after 5 years"] = df["Age"] + 5
print("\nWith new column:\n", df)

# Summary statistics
print("\nStatistics:\n", df.describe())
