# Create a function that takes a list of strings and returns the list sorted by the length of the strings$

def sortByLength(list):
    return sorted(list, key=len)

list = ["ab", "a", "abc", "abcdefg", "a", "abcedef", "abcde", "abcd"]
print(sortByLength(list))