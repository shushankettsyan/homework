# number = input("tell me a number I'll return the half of it")
# try:
#     half = int(number) / 2
#     print(half)
# except ValueError:
#     print("qqqq")


# num_1 = int(input("tell me a number to devide 4 with"))
# try:
#     new_value = 4 / num_1
# except ZeroDivisionError:
#     print("0")

# try:
#     print(hello)
# except NameError:
#     print("name")

# input_ = input("tell me a number\n")
#
# try:
#     input_ = int(input_)
# except ValueError:
#     input_ = input("tell me a number\n")
#     try:
#         input_ = int(input_)
#     except:
#         print("okay")
#         input_1 = 1



# user_amswer = input("tell me something")
#
# try:
#     my_number = int(user_amswer)
#     value = 10 / my_number
# except:
#     print("wrong value , it's not a digit")
#     my_number = 0
# except ZeroDivisionError:
#     print("the number couldn't be 0")
#     value = 10
#
# my_number += 5
# print(value)
#
# try:
#     print(value)
# except NameError:
#     print("VALUE")







# check = True
# while check:
#     try:
#         password = input("enter the password")
#
#         if len(password) < 8:
#             raise ValueError("it should be greater than 8")
#         for i in password:
#             if not i.isalpha():
#                 if i != " ":
#                     break
#                 else:
#
#                     raise NameError("the password could not contain a space")
#         for i in password:
#             if i.isdigit():
#                 break
#             else:
#                 raise TypeError("should contain at least one digit")
#         if password[0].islower():
#
#             raise TypeError("should start with a capital letter")
#         check = False
#     except ValueErrorn as e:
#         print(e)
#     except NameError as n:
#         print(n)
#     except Exception as exc:
#         print(exc)
# print(F"{password} is not a strong one")
