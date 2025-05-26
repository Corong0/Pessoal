import random


def start_game():
    while True:
        start = input(
            "Do you want to play? (Press Enter to play, q to quit.): ")
        if start == "":
            print("Game started.")
            break
        elif start.lower() == "q":
            print("Game Exited.")
            quit()
        else:
            print("Please enter a valid answer.")
            continue


def game():
    choices = ["rock", "paper", "scissors"]
    while True:
        player_choice = input("Rock, Paper, or Scissors?: ").lower()
        if player_choice in choices:
            computer_choice = random.choice(choices)
            print(f"Your choice was {player_choice}.")
            print(f"The computer's choice was {computer_choice}.")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper"):
                print("You won!")
            else:
                print("You lost!")

            play_again = input(
                "Do you want to play again? (Press Enter to play again, q to quit): ")
            if play_again.lower() == "q":
                print("Game exited.")
                break
        else:
            print("Please enter a valid answer.")


print("Welcome to the Rock Paper Scissors game!")
start_game()
game()
