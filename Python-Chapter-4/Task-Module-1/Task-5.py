# Task 5: Reverse a list without using built-in reverse functions

numbers = [10, 20, 30, 40, 50]

reversed_numbers = []

for index in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[index])

print("Original list:", numbers)
print("Reversed list:", reversed_numbers)
