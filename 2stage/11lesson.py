import logging

# engine_num = "1_1"
# tell_temp = int(input("tell the temp\t"))

##**the default level for logging is WARNING
# if tell_temp > 50:
#     logging.warning("tell engine tempriture is above the optimal")


# logging.warning ("the engine tempriture is above the optimal level") #will print a massange to the consol
# logging.info("the engine tempriture is raising") #wont print anything
# logging.debug(F"the {engine_num} engine tempriture is raising") #wont print anything
# logging.error(F"can't turn off {engine_num} engine") #will print the massage to the

##-------------------------------------------------------------------------------
##----loging info a file, and defineing the level----

# logging.basicConfig(filename = "tempritures.log", level = logging.DEBUG)
# logging.debug("this message should go to the log file")
# logging.info("so should this")
# logging.warning("and this too")
# logging.error("and non-ASCII stuff too")

##-------------------------------------------------------------------------------

logging.basicConfig(filename = "example.log", filemode = "w", level = logging.DEBUG)

logging.debug("this message should go to the log file")
logging.info("so should this")
logging.warning("and this too")
logging.error("and non-ASCII stuff too")

##----format----
# logging.warning("%s before you %s ", "look", "leap")


##-------------------------------------------------------------------------------

# logging.basicConfig(format = "%(levelname)s:%(message)s", level = logging.DEBUG)
# logging.warning("and this too")
# logging.error("and non-ASCII stuff too")

##-------------------------------------------------------------------------------
##** format@ ashxatum a menak % nerov
# logging.basicConfig(format = "%(asctime)s:::%(message)s",filename = "example.log")
# logging.warning("is the tempriture 100?")

##-------------------------------------------------------------------------------
# logging.basicConfig(format = "%(asctime)s:::%(message)s",filename = "example.log")
# logging.warning("is the tempriture 100?")
#
# dict_ = {"key1":5}
#
# try:
#     a = dict_["key2"]
#
# except KeyError:
#     logging.error("key2 is not exist", exc_info = True)
#
# print("\nthat was error message")



##-------------------------------------------------------------------------------
def my_func(*argv):
    a = 0
    for arg in argv:
        a += arg
    return a

my_func()
