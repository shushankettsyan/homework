import math
#task1
#version1
print("Area of triangle")
def function (a,h):
    area = int(a * h / 2)
    return area

a = int(input("enter the base\n"))
h = int(input("enter the height\n"))
print("area =",function(a,h))

#version2
print("\n")
print("Area of triangle")
def function (a,b,c):
    area = float(a * b * math.sin(c))
    return area

a = int(input("enter the base\n"))
b = int(input("enter the height\n"))
c = int(input("enter the angle degree\n"))

print("area =",function(a,b,c))



#task2
print("\n")
print("\n")
print("reverse")
x = input("enter the word\n")
x = x[::-1]
print(x)


#task3
#version1
print("\n")
print("\n")
print("calculate the number of uppercase and lowercase letters")
string = str(input("enter the word\n"))
upperLetters = 0
lowerLetters = 0
for i in string:
    if i.isupper():
        upperLetters += 1
    elif i.islower():
        lowerLetters += 1
print(F'the number of uppercase letters is {upperLetters}\nthe number of lowercase letters is {lowerLetters}')


#version2
print("\n")
print("calculate the number of uppercase and lowercase letters")
def function ():
    upperLetters = 0
    lowerLetters = 0
    word = str(input("enter the word\n"))
    for i in word:
        if i.isupper():
            upperLetters += 1
        elif i.islower():
            lowerLetters += 1
    print(F'the number of uppercase letters is {upperLetters}\nthe number of lowercase letters is {lowerLetters}')
print(function())






#task4
print("\n")
print("\n")
print("palindrome")
def palindrome(x):
    return x==x [::-1]

x = input("enter the word\n")
if palindrome(x):
    print(f"{x} is palindrome")
else:
    print(f"{x} isn't palindrome")
