schedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
n = 0
for v in schedule.values():
    if v is not None:
        n += len(v)
print(n)
# another case
schedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
n = []
for v in schedule.values():
    if v is not None:
        n.extend(v)
print(len(n))