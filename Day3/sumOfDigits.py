num = int(input("Enter a number : "))

sum = 0

while(num > 0):
    rem = num%10
    sum += rem
    num = num // 10

print("The sum of Digits = ", sum)
