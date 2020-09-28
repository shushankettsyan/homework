from random import randint
import random
#task 1
#version1
print('factorial')
num = int(input("enter number\n"))
factorial = 1
if num > 0:
    for i in range(1,num + 1):
        factorial = factorial * i
print(factorial)

#version2
print("\n")
print('factorial')
num = int(input("enter number\n"))
factorial = 1
while num != 0:
    factorial *= num
    num -= 1
print(factorial)


#task2
print("\n")
print("\n")
print("\tmagic 8 ball")
q1 = int(input("1.should you go to a party\n\tenter 1 or 2\n"))
r1 = random.randint(1,2)

if q1 == r1 == 1:
    print("Sure, don't forget to bring your own alchohol")
else:
    print("I don't think so")

q2 = int(input("\n2.Should you buy a new Iphone\n\tenter 1 or 2\n"))
r2 = random.randint(1,2)

if q2 == r2 == 1:
    print("yes")
else:
    print("no")

q3 = int(input("\n3.Should you go for a walk\n\tenter 1 or 2\n"))
r3 = random.randint(1,2)

if q3 == r3 == 1:
    print("yes")
else:
    print("no")







#task3
print("\n")
print("\n")
print("Fibonacci 0-50")
a = 0
b = 1
while b < 50:
     print(a, end = " ")
     print(b, end = " ")
     a += b
     b += a



#task 4
print("\n")
print("\n")
print("Rock-Paper-Scissors")
check = "yes"
score = 0
round = 0
computer = 0
while check == "yes":
    user = int(input("1:Rock\n2:Paper\n3:Scissors\n"))
    random = randint (1,3)

    if user == random:
        score += 1
        round += 1
        print("you win")
    else:
        computer +=1
        round += 1
        print("you lose")

    check = input("do you want to play again: enter yes for yes\n")

print(F"your score={score}\ncomputer score={computer}\nplayed times={round}")





#task5
print("\n")
print("\n")
result_str="";
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)
