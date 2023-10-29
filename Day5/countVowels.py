# Write a function to count the number of vowels in a  given string.
def countVowels(string):
    str = string.lower()
    count = 0
    for char in str:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    return count


string = "Hello, My name is sachin singh"
print("Number of Vowels : ", countVowels(string))
