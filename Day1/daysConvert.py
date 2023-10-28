# Write a program that converts a given number of days into years, weeks, and days+
totalDays = int(input("Enter number of days : "))

years = totalDays // 365
remaining_days = totalDays % 365
weeks = remaining_days // 7
days = remaining_days % 7

print(f"{totalDays} Days = {years} Years, {weeks} Weeks & {days} Days")
