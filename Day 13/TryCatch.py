# Let's try and catch

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("You have typed an invalid number.")
    age = int(input("Enter your age: "))

if age>18:
    print("You can drive.")
