# Implement a function that takes two lists and returns their union (all unique elements from both lists).

def unionList(list1, list2):
    result = list(set(list1+list2))
    return result

# Test the function with some values
print(unionList([1, 2, 3], [3, 5, 6]))


