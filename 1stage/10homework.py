# x="";
# for row in range(0,7):
#     for column in range(0,7):
#         if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):
#             result_str=result_str+"*"
#         else:
#             result_str=result_str+" "
#     result_str=result_str


list_1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
list_0 = []
for i in list_1:
    if i not in list_1:
        list_0.append(i)
print(list_0)        
