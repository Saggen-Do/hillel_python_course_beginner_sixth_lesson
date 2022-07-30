first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
merged_dict = {**first, **second, **third, **fourth, **fifth}
merged_dict2 = first | second | third | fourth | fifth
print(merged_dict)
print(merged_dict2)