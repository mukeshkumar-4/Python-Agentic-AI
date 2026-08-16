# Task 7: Read a CSV file and print the top 5 rows

import pandas as pd

# Make sure employees.csv is in the same folder as this Python file.
employees_data = pd.read_csv('/Users/mukeshkumarr/VS-Code/Python-Agentic-AI/Python-Chapter-4/employees.csv')

print("Top 5 rows:")
print(employees_data.head(5))
