# Write a Python program to count the occurrences of each element in a given list
from collections import Counter


def count_occurrences(input_list):
    return Counter(input_list)


# Example usage:
input_list = [1, 2, 3, 4, 2, 3, 1, 5, 6, 7, 5, 2]
occurrences = count_occurrences(input_list)

for element, count in occurrences.items():
    print(f"The element {element} occurs {count} times.")
