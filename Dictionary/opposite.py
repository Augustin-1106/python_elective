x = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
opposite_dict = {value: key for key, value in x.items()}

print(opposite_dict)