# Task 8: Create a DataFrame from a Python dictionary

import pandas as pd

employees = {
    "Name": ["Arun", "Priya", "Karthik", "Divya", "Rahul"],
    "Age": [25, 32, 28, 35, 30],
    "City": ["Chennai", "Bangalore", "Hyderabad", "Chennai", "Mumbai"],
    "Salary": [45000, 65000, 52000, 72000, 58000]
}

employees_df = pd.DataFrame(employees)

print(employees_df)
