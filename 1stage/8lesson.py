# def my_function(a,b):
#     #print(c)
#
# #my_function(4,5)
# v = my_function(5,5)
# print(v)


# def my_function(a):
#     b = f"happy bday dear {a}"
#     return b
#
# greeting = my_function("Shushan")
# print(greeting)



#  def my_function():
#     a = input("tell me the name")
#     b = f"happy bday dear {a}"
#     return b
#
# greeting = my_function("Shushan")
# print(greeting)


# v = "hello"
# def sum_1(a,b,c=0):
#     global v
#
#     v = a + b + c
#     print(v)
#
#
# #sum_1(2,1)
# sum_1(2,1,4)
#
# print(v)





# v = "hello"
# def sum_1(a,b,c=0):
#     global v
# #error str hello+tiv
#     ag = v + a + b + c
#     #print(v)
#
# sum_1(2,1,4)
#
# print(v)

# from random import randint
#
# help(randint)






def volume_(a,b,c=1):
    volume = a * b * c
    print(volume)

a_input = int(input("tell me parameters"))
b_input = int(input("tell me parameters"))
c_input = int(input("tell me parameters"))
volume_(a_input, b_input, c_input)
