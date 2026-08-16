# Task 4: Count vowels in a string

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for character in text:
    if character in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)
