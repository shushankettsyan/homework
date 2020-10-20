class Students(object):
    def __init__(self,grade):
        self.__grade = grade
    # def __str__(self): #str()
    # 	return "this is an object of Student and it's grade is {}".format(self.__grade)
    def __repr__(self):
    	return "class Student {}".format(self.__grade)
    # def __int__(self):
    # 	return int(self.__grade)
    # def __bool__(self):
    # 	if self.__grade > 10:
    # 		check = True
    # 	else:
    # 		check = False
    # 	return check
    # def __del__(self):
    #     print(self, "object is  succesfully deleted")
    def __eq__(self,other):
    	check = type(self.__grade) == type(other)
    	return check
    def get_grade(self):
        return self.__grade
    def set_grade(self, new_grade):
        self.__grade = new_grade
a = Students(10.5)
# print(bool(a))
print(a ==5)
a = Students(5)
# print(bool(a))
print(a)
# a = Students(10)
# a = Students(11)
# print(str(a))
#b = Students(50)
# print(a.get_grade())
