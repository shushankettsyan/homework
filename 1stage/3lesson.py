# myinput = input('tell me something ')
# print(myinput)
from datetime import datetime
current_time = datetime.now()
year = current_time.year
# import math
# p = 3.14
# r = float(input('r'))
# s = p * r ** 2
# l = 2 * p * r
# print(s)
# print(l)

#
# name = input('your name')
# surename = input('surename')
# print(name, surename)

y = float(input('tell me your age'))
v = (year-y) + 100
print(v)

# import variables
#same folder
from variables import year, month, day
#other folder
#from other_folder import
from datetime import datetime

current_time = datetime.now()
# print("today's date is",variables.year,variables.month,variables.day)


#other folder
#from other_folder import

# print("today's date is",year,month,day)
print(current_time)
