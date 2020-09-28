x = {'c1': 'Red', 'c2': 'Green', 'c3': None}

for key in x:
    if x[key] == None:
        key.pop()
