
# Implement a program that swaps the values of two variables.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(f"Before Swaping N1 = {num1} & N2 = {num2}")
'''
temp = num1
num1 = num2
num2 = temp
'''
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After Swaping N1 = {num1} & N2 = {num2}")
