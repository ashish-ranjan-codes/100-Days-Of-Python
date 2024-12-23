# Functions with multiple inputs

def your_details(name, age, location):
    print()
    print(f"Hey! Your name is {name}.")
    print(f"Your age is {age}.")
    print(f"Your location is {location}.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")

your_details(name, age, location)

#also this way
your_details(age=age, location=location, name=name)