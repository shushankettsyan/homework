# #task1
# celsius = float(input('Enter temperature in celsius:'))
# fahrenheit = (celsius * 1.8) + 32
# print('\t\t\t\t',fahrenheit)
#
#Task2
# a = 5
# b = 6
# c = 7
#2.1
# x = (a + b + c) / 3
# print('\n',x)
#
# #2.2
# y = a ** c + b ** c
# print('\n',y)
#
# #2.33 
# z = (a + b) ** c
# print('\n',z)

#2.4
#print('\n',str(a) + str(b) + str(c) ,'+', str(a) + '*' + str(b) + '*' + str(c))
# x = (str(a) + str(b) + str(c))
# y = (int(x) + a*b*c)
# print('\n',y)
# # #task3
print('\n\n   this program will help you to find your shirt size''\n   please fill the form')
print('\n')

mass = float(input('enter your weight (kg):'))
height = float(input('enter your height (cm):'))
bmi = (mass / height ** 2)*10**4
print('\n\t\t',bmi)

a = '(15-16)'
b = '(16-18.5)'
c = '(18.5-25)'
d = '(25-30)'
e = '(30-35)'
f = '(35-40)'
print('\n\t\t\tRESULTS')
print('\n\tXS',a,'\tM',c,'\tXL',e,sep = ' ')
print('\n\tS',b,'\tL',d,'\tXXL',f,sep = ' ')
