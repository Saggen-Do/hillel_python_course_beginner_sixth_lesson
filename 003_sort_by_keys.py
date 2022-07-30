dict_list = {4: 'forth', 1: 'first', 5: 'fifth', 8: 'eight', 11: 'eleventh'}
w = dict(sorted(dict_list.items(), key=lambda x: x[0]))
print(w)