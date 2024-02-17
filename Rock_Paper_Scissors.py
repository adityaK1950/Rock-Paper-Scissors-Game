# Rock Paper  Scissors Game
import random

def print_result(user_action, computer_action, result):
    print(f"\nYou chose {user_action}, computer chose {computer_action}.")
    print(result)

def play_again():
    return input("Play Again? (y/n): ").lower() == "y"

while True:
    user_action = input("Enter your choice (rock, paper, or scissors): ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        result = f"Both players selected {user_action}. It's a Tie!"
    elif (
        (user_action == "rock" and computer_action == "scissors") or
        (user_action == "paper" and computer_action == "rock") or
        (user_action == "scissors" and computer_action == "paper")
    ):
        result = f"{user_action.capitalize()} crushes {computer_action}. You Win!"
    else:
        result = f"{computer_action.capitalize()} covers {user_action}. You Lose..."

    print_result(user_action.capitalize(), computer_action.capitalize(), result)

    if not play_again():
        break
