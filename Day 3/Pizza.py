# let's buy a pizza

print("*** Welcome to Dominos Pizza ***")
print()

size = input("What size pizza do you want? S, M or L ")

if size == 'S' or size == 'M' or size == 'L':
    if size == 'S':
        bill = 15
    elif size == 'M':
        bill = 20
    else:
        bill = 25
    
    pepper = input("Do you want pepper? Y/N ")
    cheese = input("Do you want extra cheese? Y/N ")

    if pepper == 'Y': bill += 3
    if cheese == 'Y': bill += 1

    print(f"Your total bill is ${bill}")

else:
    print("Sorry, this size is not available.")