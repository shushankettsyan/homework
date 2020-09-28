import random
# for i in range(1,11):
#     print(f"this is for{i}")
#     for j in range(1,11):
#         print(F'{i}x{j}={i*j}')


#
# for i in range(1,12):
#     if i <= 6:
#         for j in range(i):
#             print(j*str(j))
#     else:
#         for j in range(5,0,-1):
#             print(j*str(j))
#
# for i in range(1,12):
#     print(i*"*")
#     if i ==6:
#         for j in range(5,0,-1):
#             print(j*"*")
#         break


# a = 7
# b = 5
# while a > b:
#     print(F"{a} > {b}")
#     a -= 1







# password = input("tell me the password \n")
#
# while len(password) < 8:
#     password = input("tell me the password \n")


# #version1
# while True:
#     password = input("tell me password")
#
#     if len(password) > 8:
#         if "." in password:
#             break
# print("it's a good one!")



# #version2
# a = True
# while a:
#     password = input("tell me pass\n")
#
#     if len(password) > 8 and "." in password
#             a = False
# print("it's a good one ")




# #random
# import random
# a = random.randint(1,3)
# print(a)










#
# i = 0
# user_score = 0
# while i <=5:
#     user_answer = int(input("guess the number\n"))
#     ramdom_number = random.randint(1,5)
#
#     if user_answer == ramdom_number:
#         user_score += 1
#
#     i +=1
#
# print(F"your score is {user_score}")





user_check = "y"
user_score = 0
rounds = 0
while user_check == "y":
    user_answer = int(input("guess the number\n"))
    ramdom_number = random.randint(1,5)

    if user_answer == ramdom_number:
        user_score += 1

    user_check = input("do you want to play again: y for yes!")
    rounds += 1
print(F"your score is {user_score} you have played {rounds} time")
