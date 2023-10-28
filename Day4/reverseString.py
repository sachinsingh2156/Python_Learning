# Implement a function that reverses a given string.
def reverse(str):
    rev = str[::-1]
    return rev


str = input("Enter the String : ")
print(f"The reverse of {str} = {reverse(str)}")
