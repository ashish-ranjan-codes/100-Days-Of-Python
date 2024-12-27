# Let's build Higher Lower Game

from GameData import data
import random

print("\n*** Higher Lower Game ***\n")

run_game = True
account1 = random.choice(data)
account2 = random.choice(data)

#function to fetch data
def format_data(account):
    account_name = account['name']
    account_job = account['job']
    return f"{account_name}, a {account_job}"

score = 0

while run_game:
    account1 = account2
    while account1 == account2:
        account2 = random.choice(data)

    print(f"Compare A: {format_data(account1)}")
    print("Vs")
    print(f"Compare B: {format_data(account2)}")

    user_result = input("\nWho has more followers?\nType A or B: ").upper()

    followers1 = account1['followers']
    followers2 = account2['followers']

    if followers1 > followers2:
        result = 'A'
    else:
        result = 'B'

    if user_result == result:
        score += 1
        print(f"You won!\nYour score is {score}\n")
    else:
        run_game = False
        print("You lost.\n")