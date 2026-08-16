# Task 9: Replace missing values with the column's mean

import pandas as pd
import numpy as np

employees = {
    "Name": ["Arun", "Priya", "Karthik", "Divya", "Rahul"],
    "Age": [25, np.nan, 28, 35, np.nan],
    "Salary": [45000, 65000, np.nan, 72000, 58000]
}

employees_df = pd.DataFrame(employees)

print("Before replacing missing values:")
print(employees_df)

# Fill missing numeric values with their respective column mean.
numeric_columns = employees_df.select_dtypes(include="number").columns

for column in numeric_columns:
    employees_df[column] = employees_df[column].fillna(employees_df[column].mean())

print("\nAfter replacing missing values with column mean:")
print(employees_df)
