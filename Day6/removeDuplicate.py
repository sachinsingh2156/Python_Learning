# Given a list of names, remove all duplicate names and print the unique names$

name = ["sachin", "singh", "Minal", "singh", "abhishek","raj","mishra","raj"]

nameSet = set()
result = []
for i in name:
    if i.lower() not in nameSet:
        result.append(i)
        nameSet.add(i)

print("Unique Names are : ",result)

'''Method 2'''
# name = ["sachin", "singh", "Minal", "singh", "abhishek","raj","mishra","raj"]

# nameSet = []
# result = []
# for i in name:
#     if i.lower() not in nameSet:
#         result.append(i)
#         nameSet.append(i)

# print("Unique Names are : ",result)


