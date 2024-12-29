# Let's build Coffee Machine
from Menu import menu
from Menu import resources

#check if resources are sufficient
def is_resource_sufficient(order_ingredients):
    """Returns True if ingredients are sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry! There is not enough {item}.")
            return False
    return True

#coin processing
def process_coins():
    """Returns the total calculated coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

#check sufficient money
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded!")

#make coffee
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
#Main program
print("\n*** Hey! I am your Coffee Machine ***")

machine_switch = True
profit = 0

while machine_switch:
    choice = input("\nWhat would you like? (espresso/latte/cappucino) ")
    if choice == 'off':
        machine_switch = False
    elif choice == 'report':
        print()
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} gm")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
