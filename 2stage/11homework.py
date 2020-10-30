import random
import logging


for i in range(50):
    x = random.randint(0,50)


if 0 <= x <= 9:
    logging.basicConfig(format = "%(asctime)s:::%(message)s", filename = "idk.log", filemode = "w", level = logging.DEBUG)
    logging.debug("random number is between 0 and 9 ")


if 10 <= x <= 19:
    logging.basicConfig(format = "%(asctime)s:::%(message)s", filename = "idk.log", filemode = "w", level = logging.INFO)
    logging.info("random number is between 0 and 9 ")


if 20 <= x <= 29:
    logging.basicConfig(format = "%(asctime)s:::%(message)s", filename = "idk.log", filemode = "w", level = logging.WARNING)
    logging.warning("random number is between 0 and 9 ")

if 30 <= x <= 39:
    logging.basicConfig(format = "%(asctime)s:::%(message)s", filename = "idk.log", filemode = "w", level = logging.ERROR)
    logging.error("random number is between 0 and 9 ")

if 40 <= x <= 50:
    logging.basicConfig(format = "%(asctime)s:::%(message)s", filename = "idk.log", filemode = "w", level = logging.CRITICAL)
    logging.critical("random number is between 0 and 9 ")
