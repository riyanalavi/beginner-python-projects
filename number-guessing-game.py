import random


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Number Guessing Game")
    print("I'm thinking of a number from 1 to 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if not 1 <= guess <= 100:
                print("Please enter a number from 1 to 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"You guessed it in {attempts} attempts!")
                break

        except ValueError:
            print("Please enter a whole number.")


if __name__ == "__main__":
    play_game()