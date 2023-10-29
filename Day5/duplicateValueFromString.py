# Write a function to remove all duplicate characters from a given string

def rmDuplicate(sentence):
    result = ""
    for char in sentence:
        if char not in result:
            result += char
    return result


str = "Hello my name is sachin singh."
print(rmDuplicate(str))
