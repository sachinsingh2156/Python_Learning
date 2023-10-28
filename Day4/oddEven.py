# Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly"
def isEven(num):
    if (num % 2 == 0):
        print("It is a even number")
    else:
        print("It is a odd number")


num = int(input("Enter the number : "))
isEven(num)
