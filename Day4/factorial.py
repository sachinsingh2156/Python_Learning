# Implement a function that returns the factorial of a given number using recursion"
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


num = int(input("Enter the number : "))
print(f"The factorial of {num} = ", factorial(num))
