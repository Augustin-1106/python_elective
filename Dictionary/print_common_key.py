D1 = {'a': 1, 'b': 2, 'c': 3}
D2 = {'b': 4, 'c': 5, 'd': 6}

common_keys = set(D1.keys()) & set(D2.keys())

for key in common_keys:
    print(key)