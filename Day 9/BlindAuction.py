# Blind Auction program

print("\n*** Welcome to the Blind Auction ***")
bid_owners = {}

continue_bid = True

while continue_bid:
    name = input("\nWhat's your name? ")
    bid = int(input("How much you want to bid? $"))
    
    #adding into dictionary
    bid_owners[name] = bid

    restart = input("\nIs there anyone else to bid? (Yes/No) ").lower()
    if restart == 'no':
        continue_bid = False

winner_bid = 0
winner = ''
for key in bid_owners:
    if bid_owners[key] > winner_bid:
        winner_bid = bid_owners[key]
        winner = key

print(f"\nThe winner is {winner} with a bid of ${winner_bid}.")