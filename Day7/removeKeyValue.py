# Implement a function that removes a key-value pair from a dictionary􏰈
def remove_key_value_pair(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

fruit = {
    "Apple" : 1,
    "Banana" : 2,
    "Cherry" : 3,
    "grapes" : 4
}

print(fruit)
remove_key_value_pair(fruit,"Banana")
print(fruit)