from file import rate
from datetime import datetime
current_time = datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day
hour = current_time.hour
minute = current_time.minute


#task1
print('\n\tkm to miles converter')
km = float(input('km'))
miles = km / 1.609344
print('\n',miles)

#task2
print('\n\n')
print('\tamd to usd converter')
amd = float(input('amd'))
usd = rate * amd
print('\n',usd)

#task3
print('\n\n')
print("\tthis program will tell you in which year you'll become 100 yo")
y = float(input('your age'))
x = (100 - y) + year
print("\n",x)

#task4
print('\n\n')
print('\tenter your height and programm will tell you your optimal weight')
height = float(input('your height'))
optimal_weight = height ** 2 * 21.75 * 10 ** -4
print('\n',optimal_weight)

#task5
print('\n\n')
print('\tyou will get the sum of the first symboles')
y = input('year')[::-1]
m = input('month')[::-1]
d = input('day')[::-1]

x = int(y) % 10 + int(m) % 10 + int(d) % 10
print('\n',x)

#task6
print('\n\n')
print("\tenter your date of birth and this program will tell you how many minutes you've lived ")
y = float(input('year'))
m = float(input('month'))
d = float(input('day'))

k = (((year * 12 + month) * 365/12 + day) - ((y * 12 + m) * 365/12 + d)) * 24 * 60 + hour + minute
print('\n',k)
