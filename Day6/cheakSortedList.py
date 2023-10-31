# Write a program that checks if a given list is sorted in ascending order$

list1=[2,4,6,8,1,3,6,9,5]
list2=[1,2,3,4,5,6,7,8,9]

def cheakSorted(list):
    for i in range (len(list)-1):
        if list[i]>list[i+1]:
            return False
    return True

print(cheakSorted(list1))
print(cheakSorted(list2))