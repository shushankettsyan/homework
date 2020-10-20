# class Text:
# 	def __init__(self,age):
# 		self.name = input("tell something\n")
# 		self.age = age
#
# 	def printing(self):
# 		print(self.name)
# 		print(self.age)
#
# my_obj = Text(18)
# my_obj2 = Text(20)
#
# my_obj.printing()
# my_obj2.printing()
#
#
#
# class Triangle:
# 	def __init__(self):
# 		s1 = int(input(""))
# 		s2 = int(input(""))
# 		s3 = int(input(""))
#
# 	def area(self):




class Vehicle:
	def __init__(self,seats):
		self.seats = seats


	def print_seats(self):
		print(self.seats)

class Car(Vehicle):
	def __init__(self, name, color, seats):
		self.name = name
		self.color =  color
		Vehicle.__init__(self, seats)

		self.real_seats = self.seats - 1


bmw = Car("bmw", "red", 9)

print(bmw.name, bmw.color, bmw.seats, bmw.real_seats)
bmw.print_seats()
print(bmw)
print(bmw.__dict__)




class Bicycle(Vehicle):
	def __init__(self, color, brand, wheel, seats):
		self.color = color
		self.brand = brand
		self.wheel = wheel
		Vehicle.__init__(self,seats)

bi = Bicycle("green", "kawasaki", 2, 2)
print(bi.__dict__)
