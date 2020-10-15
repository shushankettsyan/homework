#task1
class Circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14

    def perimeter(self):
        return 2 * self.r * 3.14

num = input("enter a number")
num_ = Circle(float(num))
print(num_.area())
print(num_.perimeter())



#task2
class Person:
  def __init__(self, firstname, lastname, year, grade):
    self.firstname = firstname
    self.lastname = lastname
    self.year = year
    self.grade = grade

class Student(Person):
    def __init__(self, firstname, lastname, year, grade):
        Person.__init__(self, firstname, lastname, year, grade)

student = Student("John", "adams", "1998", "9")
print(student.__dict__)
