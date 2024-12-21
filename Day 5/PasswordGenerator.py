# Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','$','%','^','&','*','(',')','+','-','_']

print("*** Welcome to Paswword Generator ***")
n_letters = int(input("How many letters you want in password? "))
n_numbers = int(input("How many numbers you want in password? "))
n_symbols = int(input("How many symbols you want in password? "))

# easy level
# temp_password = ''
# for i in range(n_letters):
#     temp_password += random.choice(letters)

# for i in range(n_numbers):
#     temp_password += str(random.choice(numbers))

# for i in range(n_symbols):
#     temp_password += random.choice(symbols)

# password = random(temp_password)
# print(password)

#hard level
temp_password = []
for i in range(n_letters):
    temp_password.append(random.choice(letters))

for i in range(n_numbers):
    temp_password.append(str(random.choice(numbers)))

for i in range(n_symbols):
    temp_password.append(random.choice(symbols))

random.shuffle(temp_password) #shuffline the password list

password = ''
for char in temp_password:
    password += char

print(f"Your suggested password is {password}")
