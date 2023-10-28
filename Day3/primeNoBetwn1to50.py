# Create a loop that prints all prime numbers between 1 and 50)

import math as ma

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    sqrt_num = int(ma.sqrt(num)) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True

for num in range(2, 51):
    if is_prime(num):
        print(num)
