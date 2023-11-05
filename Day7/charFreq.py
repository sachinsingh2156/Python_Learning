def count_chars(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


string = input("Enter a string: ")
print(count_chars(string))
