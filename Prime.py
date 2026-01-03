import math

def prime_num(num):
    if num <= 1:
        print("It is prime")
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0 :
            print(f"The number is not prime {num}")
        else:
            print(f"The number is prime {num}")

prime_num(7)