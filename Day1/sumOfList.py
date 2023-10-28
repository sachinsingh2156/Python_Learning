# Given a list of integers, find the sum of all positive numbers+
'''list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for x in list:
    sum += x

print("The sum = ", sum)'''

list = [1,2,3,4,5,-2,7,-8,9,-10]
sum = 0
for x in list:
    if x > 0:
        sum += x

print("The sum = ", sum)
