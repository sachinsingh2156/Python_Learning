
#  Implement a program that checks if a given string is a palindrome􏰌
a = input("Enter a String : ")
rev = a[::-1]
if a == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
