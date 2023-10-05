p = int(input("Enter the principle amount : "))
t = int(input("Enter the time period in year : "))
r = int(input("Enter the rate of interest : "))
Amt = p * (pow((1 + r / 100), t))
CI = Amt - p
print("The compound interest is : ", CI)
