print("hi")
import random

# Generate a random number between 1 and 1000
secret_number = random.randint(1, 1000)

guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 1000"))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You guessed it!")

print("Game over!")
