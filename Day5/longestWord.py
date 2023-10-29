# Write a Python program to find the length of the longest word in a sentence

str = "Hello my name is sachin singh. I am from Nepal"

strArr = str.split()
max = strArr[0]

for i in strArr:
    if (len(i) > len(max)):
        max = i

print(max)
print(len(max))
