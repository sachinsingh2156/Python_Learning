# Write a Python function to check if a given string is a palindrome"
def palindrome(string):
    rev = string[::-1]
    if (string == rev):
        print("It is a palindrome")
    else:
        print("It is a not palindrome")


str = input("Enter the string : ")
palindrome(str)
