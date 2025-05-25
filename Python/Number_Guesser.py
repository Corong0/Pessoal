import random

print("Welcome to the number guessing game!")
print("The computer will select a random number and tell you if you are close or not.")


MIN_R = 1
MAX_R = 100


random_number = random.randrange(MIN_R, MAX_R)
# print(random_number)   # --- This enables you to see the hidden number.


def start_game():
    while True:
        strt = input(
            "The computer has selected the number, do you wish to start? (Press \"enter\" to start, \"q\" to Quit.): ")
        if strt.lower() == "":
            break
        elif strt.lower() == "q":
            quit()
        else:
            print("Please enter a valid awnswer.")


start_game()


def user_guess():
    while True:
        guess = input(
            "What is your guess? (Press \"q\" at any time to quit.) ")
        if guess.lower() == "q":
            print("Game exited.")
            quit()
        try:
            guess_int = int(guess)
        except ValueError:
            print("Please enter a valid number")
            continue
        if guess_int == random_number:
            print("You got it!")
            break
        else:
            print("That isn't it.")
            difference = abs(guess_int - random_number)

            if difference <= 2:
                print("Very Hot!")
            elif difference <= 5:
                print("You are hot!")
            elif difference <= 7:
                print("Warm")
            elif difference <= 10 and difference >= 15:
                print("Chilly")
            else:
                print("Really cold")


user_guess()

print("Congrats, you won!")
print("The number was", random_number)
