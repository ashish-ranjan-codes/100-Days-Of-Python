# check if a number is prime or not

def check_prime(num):
    if num<2:
        return False
    if num==2:
        return True
    
    for i in range(2, (num//2)+1):
        if num%i==0:
            return False
        
    return True

#main program

n = int(input("Enter a number: "))
if (check_prime(n)):
    print(f"{n} is Prime.")
else:
    print(f"{n} is not Prime.")