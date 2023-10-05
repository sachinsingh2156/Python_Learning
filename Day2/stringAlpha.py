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
