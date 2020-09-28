#task1
print("duplicate numbers remover")
x = []
numbers = [1,1,1,2,3,3,4,4,4,5,6,6]
for i in numbers:
    if i not in x:
        x.append(i)
print("\t",x)




#task2
print("\n\ncommon elements between 2 lists")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = []
for i in a and b:
    if i in a and b:
        x.append(i)
print("\t",x)




#task3
print("\n\nlist less than 5")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print("\t",i)




#task4
print("\n\nreverse")
def function(x):
    txt = x.split()
    txt.reverse()
    print("\t",txt)
txt = input("enter something")
function(txt)




#task5
#version1
print("\n\nreverse")
x = (1,2,3,"a","b","c",True)
x = x[::-1]
print("\t",x)


#version2
x = (1,2,3,"a","b","c",True)
x  = tuple(reversed(x))
print("\n\t",x)
