# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)􏰌
def isPangram(string):
    alphabet = "abcdefghjklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return "False"
    return True


a = input("Enter the string :")
if (isPangram(a) == True):
    print("This is a Panagram")
else:
    print("This is not a Panagram")
