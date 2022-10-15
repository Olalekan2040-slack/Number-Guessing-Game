import random
from random import Random, randint, random

try:
    random_number = randint(1,9)
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        if random_number % 2 == 0:
            print("Hint: The number is an even number")
        elif random_number % 3 == 0:
            print("Hint: The number is a prime number")
        elif random_number % 2 == 1:
            ("Hint: The number is an odd number")
        else:
            pass
        guess = int(input("Guess a number between 1 and 9: "))
        guess_count +=1
        if guess == random_number:
            print("You won!")
            break
        elif guess_count < 2:
            print("Try again 2 more times!")
        elif guess_count < 3:
            print("Try again 1 more time!")
        else:
            print("You failed!")
except ValueError:
    print("Invalid Value")