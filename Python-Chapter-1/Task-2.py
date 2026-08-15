# Task 2 - Loops, Conditions, Functions and Operators
# Two examples are provided for every requested module.

# 1. while loop
count = 1
while count <= 5:
    print(count)
    count += 1

number = 10
while number >= 6:
    print(number)
    number -= 1


# 2. for loop
for i in range(1, 6):
    print(i)

for fruit in ["apple", "banana", "orange"]:
    print(fruit)


# 3. if else
age = 25
if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 45
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 4. if elif else
score = 85
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("C")

temperature = 32
if temperature > 35:
    print("Hot")
elif temperature >= 25:
    print("Warm")
else:
    print("Cool")


# 5. user defined functions without for loop, if loop
def add_numbers(a, b):
    return a + b

print(add_numbers(10, 20))

def calculate_area(length, width):
    return length * width

print(calculate_area(10, 5))


# 6. user defined functions with for loop 
def print_squares(numbers):
    for number in numbers:
        print(number ** 2)

print_squares([1, 2, 3, 4])

def print_names(names):
    for name in names:
        print(name)

print_names(["Arun", "Bala", "Kumar"])


# 7. user defined functions with for loop and if condition
def print_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

print_even_numbers([1, 2, 3, 4, 5, 6])

def print_passed_students(marks):
    for mark in marks:
        if mark >= 40:
            print(mark)

print_passed_students([35, 60, 42, 28, 75])


# 8. break
for number in range(1, 10):
    if number == 5:
        break
    print(number)

for letter in "python":
    if letter == "h":
        break
    print(letter)


# 9. continue
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)


# 10. for loop with in operator
for city in ["Chennai", "Bangalore", "Hyderabad"]:
    print(city)

for character in "Python":
    print(character)


# 11. for loop with if statement
for number in range(1, 11):
    if number > 5:
        print(number)

for word in ["python", "sql", "java", "cloud"]:
    if len(word) > 4:
        print(word)


# 12. for loop with not in operator
blocked_users = ["admin", "guest"]
for user in ["admin", "mukesh", "arun"]:
    if user not in blocked_users:
        print(user)

invalid_extensions = [".exe", ".bat"]
for file_name in ["report.csv", "script.exe", "data.xlsx"]:
    if not any(file_name.endswith(ext) for ext in invalid_extensions):
        print(file_name)


# 13. if with in operator
role = "developer"
if role in ["developer", "admin"]:
    print("Access granted")

language = "python"
if language in ["python", "java", "sql"]:
    print("Language is supported")


# 14. if with not in operator
username = "mukesh"
if username not in ["admin", "guest"]:
    print("Normal user")

file_type = ".csv"
if file_type not in [".exe", ".bat"]:
    print("Safe file type")
