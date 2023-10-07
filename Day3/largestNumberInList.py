list = [55,33,66,22,44,66,33,88,12,78,34,54,67,99,10]
max = list[0]
min = list[0]
for i in list:
    if i > max:
        max=i

    if i < min:
        min=i

print("Maximum element in the list = ",max)
print("Minimum element in the list = ",min)
