# Simple number order guesser game
import random

def number_order():
    numbers = []
    numbers_to_guess = int(input("How many numbers would you like to guess?"))

    if (numbers_to_guess < 2) or (numbers_to_guess > 9):
        raise ValueError("Please enter a positive number greater than 1 but less than 9.")
    
    numbers = list(range(1, numbers_to_guess + 1))
    random.shuffle(numbers)
    # print("Shuffled numbers to guess the order of (hidden):", numbers) # Used to check what order the listis shuffled to.

    while True:
        guess = input("Enter the numbers in the order you think they are (e.g., 1234):")

        guess_list = []
        corect = 0
        if len(guess) != len(numbers):
            print(f"Please enter exactly {len(numbers)} digits.")
            continue

        try:
            guess_list = [int(g)for g in guess]
        except ValueError:
            print("Please enter only numbers.")
            continue

        if guess_list == numbers:
            print("You guessed the order correctly!")
            break
        else:
            correct = sum(1 for a, b in zip(guess_list, numbers) if a == b)
            print(f"{correct} number(s) are in the correct position. Try again!")

number_order()