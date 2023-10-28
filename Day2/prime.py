# Write a program to check if a number is prime.
num = int(input("Enter a Number : "))
i = int(2)
isPrime = bool(True)

if(num<2):
    print('Invalid')
else:
    while(i<=(num//2)):
        if num%i==0:
            isPrime = False
            break
        i +=1

    if isPrime:
        print ("%d is Prime" % int(num))
    else :
        print("%d is not prime"%int(num))

