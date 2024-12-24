# Let's build a Calculator App

def calculator(num1, num2, sign):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1 / num2
    

want_continue = True

while want_continue:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    sign = input("Choose operation: +, -, *, / ")

    operators = ['+', '-', '*', '/']

    if sign not in operators:
        print("\nHey man! At least choose proper sign.")
    else:
        print(f"Result {calculator(num1, num2, sign)}")

    restart = input("\nWanna continue? Yes/No ").lower()
    if restart == 'no':
        want_continue = False