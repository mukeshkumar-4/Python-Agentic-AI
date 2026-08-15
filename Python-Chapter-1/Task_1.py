# Task 1 - String Functions
# Two meaningful examples for common Python string functions.

text = "  Python Data Engineering  "
email = "student@example.com"

print(text.upper())

print(text.lower())

print(text.strip())

print(text.replace("Engineering", "Analytics"))

print("Python,SQL,BigQuery".split(","))

print(" - ".join(["Python", "SQL", "BigQuery"]))

print("Python programming".find("programming"))

print("banana".count("a"))

print(email.startswith("student"))

print(email.endswith(".com"))

print("data engineering".capitalize())

print("google cloud data engineer".title())

print("Python".isalpha())

print("2026".isdigit())

print("Python2026".isalnum())

print(len("BigQuery"))

# Second examples for the same functions
name = "  mukeshkumar  "
sentence = "Python makes data processing easier"
numbers = "12345"
code = "PYTHON123"

print(name.upper())
print("DATA ENGINEERING".lower())
print(name.strip())
print(sentence.replace("easier", "faster"))
print("GCP|BigQuery|Python".split("|"))
print("/".join(["home", "user", "projects"]))
print(sentence.find("data"))
print("mississippi".count("s"))
print("developer@example.org".startswith("developer"))
print("report.csv".endswith(".csv"))
print("python".capitalize())
print("cloud data platform".title())
print("BigQuery".isalpha())
print(numbers.isdigit())
print(code.isalnum())
print(len("Cloud Composer"))
