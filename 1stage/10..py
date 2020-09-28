x = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

def list_1(x):
    list_0 = []
    for i in x:
        if type(i) != list:
            list_0.append(i)
        else:
            list_0 += list_1(i)
    return list_0
print(list_1(x))








list_1 = [0, 10, [20, 30], [60, 70, 80], [90, 100, 110, 120]]
list_0 = []

for x in list_1:
    for y in x:
        if y not in x:
            list_0.append(y)
print(list_0)











list_1 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
list_0 = []
def list_1(y):
    global list_0
    if not y:
        return []
        list = 89
    if type(y[0]) not in (list):
        return [y[0]] + list_1(y[1:])
    else:
        return list_1(y[0]) + list_1(y[1:])
print(list_1(x))










x = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

z = sum(x,[])
print(z)
