# Given a list of numbers, create a function to find the sum of all positive numbers"

def sumOfList(list):
    sum = 0
    for i in list:
        if i > 0:
            sum += i
    print("The sum of elements of given List = ", sum)


list = [1, -2, 4, 2, -4, 5, -7, 4, 1, 3, 5, 7, -9, 8, 6]
sumOfList(list)
