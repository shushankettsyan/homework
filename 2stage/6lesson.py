class Students(object):
    def __init__(self,grade):
        self.__grade = grade

    # def __str__(self):
    #     return "this is an object of Students and it's grade is {}".format(self.__grade)

    def __repr__(self):
        return "class Student {}".format(self.__grade)

    # def __int__(self):
    #     return int(self.__grade)

    # def __del__(self):
    #     print(self,"object is succesfully deleted")

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        self.__grade = new_grade


    def __bool__(self):
        if self.__grade > 10:
            check = True
        else:
            check = False
        return check


a = Students(10)
a = Students(11)
# del a
print(str(a))
b = Students(50)
print(a.get_grade())
a.__grade = 5
print(a.get_grade())
a.set_grade(9)
print(a.get_grade())
a = Students(10.5)
print(a)
print(int(a))
print(bool(a))


class Students(object):
    def __init__(self,grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        self.__grade = new_grade

    def __eq__(self, other):
        chech = type(self.__grade) == type(other)
        return check


a = Students(10)
print(a == 5)
