def noOfVowels(string):
    count = 0
    str = string.upper()
    for i in str:
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            count += 1
    return count

str = input("Enter a String: ")
print("\nNumber of Vowels are ", noOfVowels(str))
