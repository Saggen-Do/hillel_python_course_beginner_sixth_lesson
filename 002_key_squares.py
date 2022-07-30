initial_dict = {}
keys = list(range(11, 21))
for item in keys:
    initial_dict[item] = (item**2)
print(initial_dict)
print(sum(initial_dict.values()))