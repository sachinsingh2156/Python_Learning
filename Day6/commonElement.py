# Create a program that finds the common elements between two lists and stores them in a new list

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [5, 6, 7, 8, 9, 10, 11, 12]

result = list(set(list1) & set(list2))
print(result)
