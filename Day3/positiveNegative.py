#  Write a program that checks if a given number is  positive, negative, or zero.

num = int(input("Enter a Number : "))

if(num < 0):
    print("It is a Negative Integer")
elif (num == 0):
    print("It is a Zero")
else:
    print("It is a Positive Integer")