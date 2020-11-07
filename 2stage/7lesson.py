import os
import shutil

# print("this file is runnimg from",os.getcwd())

#mi hat het directory (..)
print(os.listdir(F"{os.getcwd()}/.."))

base_dir = os.getcwd()

# os.makedirs(F"{base_dir}/new_python_folder")

# os.makedirs("/Users/shushankettsyan/Desktop/homework/2stage/new_python_folder")

print("we're now in {}".format(base_dir))

os.chdir("/Users/shushankettsyan/Desktop/homework/2stage/new_python_folder")

# print("we're noe in {}".format(os.getcwd()))
#
# print(os.listdir())
#
#
# #for removing all files 1
# while os.listdir():
#     file = F"{os.getcwd()}/{os.listdir()[0]}"
#     os.remove(file)
# print(os.listdir())


# my_list = [1, 2, 3]
# #for removing all files 2
# for i in my_list:
#     my_list.remove()
#
# #for removing all files 3
# for i in my_list:
#     del i


#for remobing folder directory
# b = os.getcwd()
# a = os.chdir("..")
# # a = F"{a}/.."
# os.rmdir(b)
