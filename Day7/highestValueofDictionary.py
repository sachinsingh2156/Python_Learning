# Given a list of dictionaries, find the dictionary with the highest value for a specific key􏰈
list_of_dicts = [
    {'name': 'Alice', 'age': 25, 'score': 90},
    {'name': 'Bob', 'age': 30, 'score': 85},
    {'name': 'Charlie', 'age': 28, 'score': 95},
    {'name': 'David', 'age': 27, 'score': 80}
]
max_dict = max(list_of_dicts, key=lambda x: x['score'])
print(max_dict)
# Output: {'name': 'Charlie', 'age': 28, 'score': 95}
