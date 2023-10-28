# Create a program that checks if a given string is a  palindrome.

str = input("Enter the String : ")

rev = str[::-1]

if (str == rev):
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")
