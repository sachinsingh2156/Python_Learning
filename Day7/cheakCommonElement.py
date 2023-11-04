#  Create a program that checks if two sets have any elements in common􏰈

set1={1,2,3,4,5,6}
set2={7,8,9,10,11,12}
set3={4,5,6,7,8,9,10}
result = set1 & set3

if not result:
    print("No common element")
else:
    print("Common Elements are",result)