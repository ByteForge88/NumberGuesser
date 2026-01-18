import random

MAX_TRIES = 10

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
ENDC = "\033[0m"

def try_again():
    print("Would you like to try again?\n")
    response = input("Press 'c' to continue or press 'e' to exit: ")

    if response == "c":
        start_game()
    elif response == "e":
        print("\nHave a great day!")

def start_game():
    print("\nI'm thinking of a number between 1 and 10\n")
    random_int = random.randint(1, 10)
    tries = MAX_TRIES

    while tries > 0:
        guess = int(input("Enter a guess: "))

        if guess == random_int:
            print(GREEN + "\nYou have guessed the right number, You won!\n" + ENDC)
            try_again()
            break
        else:
            tries -= 1
            print(RED + "\nYou have guessed wrong, try again!\n" + ENDC)
            print(f"You have {tries} tries left!\n")

    if tries == 0:
        print(YELLOW + "You ran out of tries, Better luck next time!\n" + ENDC)
        print("The correct answer was " + str(random_int) + "\n")

def main():
    print("\nWelcome to the guesser name!\n")
    user_input = input("Press 'c' to continue or press 'e' to exit: ")

    if user_input == "c":
        start_game()
    elif user_input == "e":
        print("\nYou have left the game, Goodbye!\n")

main()
