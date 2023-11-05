# Create a function that takes a list of dictionaries and sorts them based on a specified key
def sort_dicts(dicts, key):
    return sorted(dicts, key=lambda x: x[key])


dicts = [{'name': 'John', 'age': 25},
         {'name': 'Jane', 'age': 30},
         {'name': 'Bob', 'age': 20}]

sorted_dicts = sort_dicts(dicts, 'name')
print('Sorted by name:', sorted_dicts)

sorted_dicts = sort_dicts(dicts, 'age')
print('Sorted by age:', sorted_dicts)
