# import json
# with open("python.txt", "r") as file:
#     read_value = file.read()
#
# print(read_value)
#
#
#  for i in file:
#      c = i.readline()
#      print(c)
#
#
#
# #------------------------------------------------------------------------------
# #--for adding--
# with open("python.txt", "r") as file:
#     read_value = file.read()
#
# print(read_value)
#
# read_value += "\ntoday is 10.22.20"
# print(read_value)
#
#
# with open("python.txt", "w") as file:
#     file.write(read_value)
#
#
#
# #------------------------------------------------------------------------------
# #--append noric add anel--
# with open("python.txt", "r") as file:
#     read_value = file.read()
#
# with open("python.txt", "a") as file:
#     file.write(read_value)
#
#
#
# #------------------------------------------------------------------------------
#--json file--
with open("python.txt", "r") as file:
    read_value = file.read()
print(read_value)

with open("json.json", "r") as file2:
    data = json.load(file2)

print(data)
print(type(data))
print("\n",data["items"][0])

#
#
# #------------------------------------------------------------------------------
# #--YAML--
