# Task 10: Filter rows where Age is greater than 30

import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Karthik", "Divya", "Rahul"],
    "Age": [25, 32, 28, 35, 40],
    "City": ["Chennai", "Bangalore", "Hyderabad", "Chennai", "Mumbai"],
    "Salary": [45000, 65000, 52000, 72000, 80000]
}

df = pd.DataFrame(data)

filtered_df = df[df["Age"] > 30]

print("Rows where Age is greater than 30:")
print(filtered_df)
