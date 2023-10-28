# Create a Python function to check if a given string is a palindrome+
s = input("Enter a String : ")
res = s[::-1]
if s == res:
    print("It is a Palindrome")
else:
    print("It is not a palindrome")
