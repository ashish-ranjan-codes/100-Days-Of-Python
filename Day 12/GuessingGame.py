# Let's build a Number Guessing Game
import random

print("\n*** Welcome to the Number Guessing Game ***")
print("I am thinking of a number between 1 and 100.")
print("Choose difficulty...")
difficulty = input("Type 'easy' or 'hard': ").lower()

actual_num = random.randint(1, 100)
attempts = 10
if difficulty == 'hard':
    attempts = 5

#main
while attempts>0:
    guess = int(input("\nMake a guess: "))
    attempts -= 1
    if guess>actual_num:
        print("Too high.\nGuess again!")
    elif guess<actual_num:
        print("Too low.\nGuess again!")
    elif guess == actual_num:
        print("Oh Wow! You won")
        break

    print(f"You have {attempts} left.")
