# Given a list of numbers, find the maximum and minimum values+


list = [2, 3, 4, 1, 5, 9, 6, 7]
max = list[0]
min = list[0]
for a in list:
    if (int(a) > int(max)):
        max = a
    if (int(a) < int(min)):
        min = a


print("Maximum = ", max)
print("Minimum = ", min)
