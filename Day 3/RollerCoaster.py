# let's decide rollar coaster ride price for individual

age = int(input("What's your age? "))

if age<=25:
    if age<=12:
        bill = 10
    elif age>12 and age<=18:
        bill = 15
    else:
        bill = 20
    
    want_photo = input("Do you want to take photo? (y/n) ")
    if want_photo == 'y':
        bill += 3

    print(f"You can ride and your bill would be {bill}")

else:
    print("Sorry! You can't ride.")