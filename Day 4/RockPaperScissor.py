# let's build rock, paper, scissors

import random
choices = ["rock", "paper", "scissor"]
your_choice = int(input("Enter your choice: "))
print("Your choice: ", choices[your_choice])
computer_choice = random.randint(0,2)
print("Computer's choice: ", choices[computer_choice])

if your_choice > computer_choice:
    print("You won.")
elif computer_choice > your_choice:
    print("Computer won")
else:
    print("Draw")


