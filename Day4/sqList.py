# Create a function to find the square of each element in a given list"
def squareOfList(list):
    sqList = []
    for i in list:
        sqList.append(i**2)
    return sqList


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The square of the list = ", squareOfList(list))
