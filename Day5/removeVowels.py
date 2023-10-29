# Given a string, write a function to remove all vowels from it and return the modified string
def removeVowels(str):
    newStr = ""
    for i in str.lower():
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            newStr += i

    return newStr


str = input("Enter the string : ")
print("The string without vowels is : \n", removeVowels(str))
