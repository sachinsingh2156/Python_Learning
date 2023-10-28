# Implement a program that converts a given number of minutes into hours and minutes􏰌
min = int(input("Enter the time in Minutes : "))

hour = min//60
remaining = min - (hour*60)

print(f"{min} Minute = {hour} Hour & {remaining} Minutes")