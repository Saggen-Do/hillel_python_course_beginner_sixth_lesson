x = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
z = set()
for i in x:
    for k, v in i.items():
        z.add(v)
print(z)
q = []
for i in x:
    for k, v in i.items():
        if v in z:
            q.append(i)
print(q)