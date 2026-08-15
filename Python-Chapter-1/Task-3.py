# Task 3 - Rock, Paper, Scissors Game

import random

choices = ["rock", "paper", "scissors"]

print("=== Rock, Paper, Scissors ===")

while True:
    try:
        player = input("Enter rock, paper, or scissors: ").strip().lower()

        if player not in choices:
            raise ValueError("Invalid choice. Please enter rock, paper, or scissors.")

        computer = random.choice(choices)
        print("Computer chose:", computer)

        if player == computer:
            print("It's a tie!")
        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            print("You win!")
        else:
            print("Computer wins!")

        again = input("Do you want to play again? (yes/no): ").strip().lower()

        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break

    except ValueError as error:
        print("Error:", error)
