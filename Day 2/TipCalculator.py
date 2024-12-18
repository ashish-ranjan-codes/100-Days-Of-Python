# Tip Calculator Project

print("Welcome to the Tip Calulator")
print()
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 5%, 10%, 15%, 20% "))
people = int(input("How much people to split the bill? "))

total_bill = bill + (bill*tip)/100
payable_bill = total_bill/5
print(f"Each person would pay ${round(payable_bill, 2)}")
