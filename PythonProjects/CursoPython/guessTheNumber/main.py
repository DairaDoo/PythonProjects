from art import logo
import random


def game():
    """"Guess the number game function"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number from 1 and 100")
    attempts = 10
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    keep_playing = True

    if difficulty == 'hard':
        attempts = 5
    elif difficulty != 'easy' and 'hard':
        keep_playing = False
        print("Wrong option")

    print(f"You have {attempts} attempts remaining to guess the number.")

    winning_number = random.randint(1, 100)

    # condition to keep the user playing until the attempts are lost or the user choose the correct answer.

    while keep_playing:

        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return  # Se puede usar el return también para finalizar el programa si este se encuentra en una función.

        user_guess = int(input("Make a guess: "))

        if user_guess > winning_number:
            print("Too high.")
            attempts -= 1
        elif user_guess < winning_number:
            print("To low.")
            attempts -= 1
        elif user_guess == winning_number:
            print(f"You got it! The answer was {winning_number}.")
            return
        if attempts != 0:
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")


game()
