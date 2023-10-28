# Write a program that calculates the factorial of a given number)
num = int(input("Enter a number : "))
factorial = 1
if(num == 0):
    factorial = 0
else: 
    for i in range (num,0, -1):
        factorial *= i

print(f"Factorial of {num} = {factorial} ")