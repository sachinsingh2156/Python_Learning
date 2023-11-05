# Implement a function that takes a list of strings and returns a set of unique characters present in all strings.

def unique_chars(lst):
    str = ""
    for i in lst:
        str += i
    return set(str)


lst = ['hello', 'world', 'python']
print(unique_chars(lst))
