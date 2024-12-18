# manipulating numbers

height = 5.2
weight = 75.6
bmi = weight / height**2

print(bmi)
print(int(bmi)) # removing decimals
print(round(bmi)) # rounding num to the nearest integer
print(round(bmi, 2)) # rounding to 2 decimal places

bmi += 1 #increment
print(bmi)
bmi -= 1 #decrement
print(bmi)

#f-strings
print(f"Your BMI is: {round(bmi, 2)}") #allows using different data types with string