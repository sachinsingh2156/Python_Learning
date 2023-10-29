# Create a list of fruits and add a new fruit to the list.
initial_fruits = input("Enter a list of fruits separated by spaces: ").split()

# Create a list from the input
fruits = list(initial_fruits)
print(fruits)

# Take input from the user for the new fruit
new_fruit = input("Enter a new fruit: ")

# Add the new fruit to the list
fruits.append(new_fruit)

# Print the updated list of fruits
print(fruits)
