# Task 4 - Word Guessing Game (Mini Hangman)

import random

words = ["python", "machine", "learning", "bridge", "computer", "database"]

print("=== Word Guessing Game ===")

word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

while wrong_guesses < max_attempts:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "    
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    try:
        guess = input("Guess one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            raise ValueError("Please enter exactly one alphabet letter.")

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    except ValueError as error:
        print("Error:", error)

else:
    print("\nGame over! You used all 6 chances.")
    print("The word was:", word)
