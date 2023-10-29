# Given a list of names, count the number of names that start with a vowel

list = ["Sachin", "abhishek", "raj", "emilia", "issac", "Openhemer"]

count = 0
for i in list:
    if (i[0].upper() == "A" or i[0].upper() == "E" or i[0].upper() == "I" or i[0].upper() == "O" or i[0].upper() == "U"):
        count += 1

print("No. of names starting with vowels are : ", count)
