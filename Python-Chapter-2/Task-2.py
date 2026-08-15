"""
Task 2: Create three Pandas DataFrames using dictionaries

"""

import pandas as pd

# ============================================================
# DATAFRAME 1 - EMPLOYEE DETAILS
# ============================================================

employee_data = {
    "Employee_ID": [101, 102, 103, 104],
    "Name": ["Mukesh", "Arun", "Priya", "Karthik"],
    "Department": ["Data Engineering", "Analytics", "Data Engineering", "Cloud"],
    "Experience": [5, 3, 4, 6]
}

df_employee = pd.DataFrame(employee_data)

print("DATAFRAME 1 - EMPLOYEE DETAILS")
print(df_employee)


# ============================================================
# DATAFRAME 2 - STUDENT DETAILS
# ============================================================

student_data = {
    "Student_ID": [1, 2, 3, 4],
    "Student_Name": ["Rahul", "Anitha", "Vijay", "Divya"],
    "Course": ["Python", "SQL", "GCP", "Python"],
    "Score": [85, 92, 88, 95]
}

df_student = pd.DataFrame(student_data)

print("\nDATAFRAME 2 - STUDENT DETAILS")
print(df_student)


# ============================================================
# DATAFRAME 3 - PRODUCT DETAILS
# ============================================================

product_data = {
    "Product_ID": [1001, 1002, 1003, 1004],
    "Product_Name": ["Laptop", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [75000, 2500, 1200, 18000]
}

df_product = pd.DataFrame(product_data)

print("\nDATAFRAME 3 - PRODUCT DETAILS")
print(df_product)