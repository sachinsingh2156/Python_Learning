list = [2,6,3,6,34,12,34,56,75,32,33,77,91,49,32,58,98,74,65,10,1]

newList =[]

for i in list:
    if(i%2 == 0):
        newList.append(i)


print("The list with Even Nubers is : \n", newList)