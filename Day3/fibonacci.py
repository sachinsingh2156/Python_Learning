# Create a program that generates the Fibonacci sequence up to a given number of terms)

n = int(input("Enter the number of terms : "))
a = 0
b = 1
c = 0

if(n==1):
    print(a)
elif(n==2):
    print (a)
    print (b)
else:
    print(a)
    print(b)

    for i in range(2,n):
        c= a+ b
        a=b
        b=c
        print(c)