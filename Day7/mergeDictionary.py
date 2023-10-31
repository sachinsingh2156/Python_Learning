# Given two dictionaries, merge them into a single dictionary􏰈

dict1 = {
    "name": "John",
    "age": 30,
    "gender": "male"
}
dict2 = {
    "Qualification": "B.tech",
    "Country": "Nepal"
}
# dict3 = dict1|dict2
# dict3 = dict1.update(dict2)
dict3 = {**dict1, **dict2}
print(dict1)
print(dict2)
print(dict3)