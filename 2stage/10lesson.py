import threading
import time
import datetime
import concurrent.futures
import multiprocessing



 def function_1():

     for i in range(10):
         time.sleep(0.5)
         print(i)

 if __name__== "__main__":
     starting_time = datetime.datetime.today()
#
#     print(starting_time)
#     print([starting_time])
#
# for i in range(4):
#     function_1()
#
# b = (datetime.datetime.today() - starting_time).seconds
# print(f"it took {b} seconds")




#-------------------------------------------------------------------------------
#--thread--

# def function_1():
#
#     for i in range(10):
#         time.sleep(0.5)
#         print(i)
#
# if __name__== "__main__":
#     starting_time = datetime.datetime.today()
#
# thread_list = []
# for i in range(4):
#     x = threading.Thread(target = function_1)
#     thread_list.append(x)
#     x.start() #for run the code
#
#
# b = (datetime.datetime.today() - starting_time).seconds
# print(f"it took {b} seconds")



#-------------------------------------------------------------------------------
#--uding thread.join function to make main thread wait for the others--
# def function_1():
#
#     for i in range(10):
#         time.sleep(0.5)
#         print(i)
#
# if __name__== "__main__":
#     starting_time = datetime.datetime.today()
#
# thread_list = []
# for i in range(4):
#     x = threading.Thread(target = function_1)
#     thread_list.append(x)
#     x.start() #for run the code
#
# for thread in thread_list:
#     thread.join() #waithing
#
# b = (datetime.datetime.today() - starting_time).seconds
# print(f"it took {b} seconds")


#-------------------------------------------------------------------------------

# def function_2(range_num):
#
#     for i in range(range_num):
#         time.sleep(0.5)
#         print(i)
# #
# if __name__== "__main__":
#     starting_time = datetime.datetime.today()
#
# thread_list = []
# for i in range(4):
#     x = threading.Thread(target = function_2, args = (5,), daemon = True)
#     thread_list.append(x)
#     x.start() #for run the code
#
# for thread in thread_list:
#     thread.join() #waithing
#
# b = (datetime.datetime.today() - starting_time).seconds
# print(f"it took {b} seconds")



#-------------------------------------------------------------------------------
# def function_3(range_num):
#
#     for i in range(range_num[0]):
#         time.sleep(0.5)
#         print(range_num[1],i)
#
# if __name__== "__main__":
#     starting_time = datetime.datetime.today()
#
# with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
#     executor.map(function_3, [(10, "a"),(10, "b"), (10, "c"),(10, "d")])
#
# b = (datetime.datetime.today() - starting_time).seconds
# print(f"it took {b} seconds")



#-------------------------------------------------------------------------------
