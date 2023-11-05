# Write a program that finds the average value of all the elements in a list of dictionaries
def avg_dict(lst):
    n = len(lst)
    if n == 0:
        return None
    sum_dict = {}
    for d in lst:
        for key, value in d.items():
            if key in sum_dict:
                sum_dict[key] += value
            else:
                sum_dict[key] = value
    return {key: value / n for key, value in sum_dict.items()}


lst = [{'a': 1, 'b': 2, 'c': 3},
       {'a': 2, 'b': 4, 'c': 6},
       {'a': 3, 'b': 6, 'c': 9}]
print(avg_dict(lst))
