# Create a function to check if a number is prime.

def isPrime(num):
    prime = bool(True)
    for i in range(2, num//2):
        if (num % i == 0):
            prime = False

    if (prime):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")


num = int(input("Enter the number : "))
isPrime(num)
