import sqlite3
from sqlite3 import Error
import os

database = os.path.join(os.getcwd(), "db", "film.db")
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
print(database)

#creating a cursor to execute commands (queries)
curs = conn.cursor()

# project_query = """ CREATE TABLE IF NOT EXISTS projects (
#                                         id integer  PRIMARY KEY,
#                                         name text NOT NULL,
#                                         begin_date text,
#                                         end_date text
#                                         ); """
#
# curs.execute(project_query)
#
# conn.commit()


# insert_query = """ INSERT INTO projects(id, name, begin_date, end_date)
# 					VALUES (1, 'python', '2020-09-01', '2020-12-01');
# 					"""
# curs.execute(insert_query)
# conn.commit()
##updating the date of created row



##------------------------------------------------------------------------------
# update_query = """ UPDATE projects
# 					SET begin_date = '2020-10-01'
# 					WHERE id = 1
# 					"""
# curs.execute(update_query)
# conn.commit()

##------------------------------------------------------------------------------
# update_query = """ UPDATE projects
# 					SET begin_date = '2020-10-01'
# 					WHERE id = 1
# 					"""
#
# with conn:
#     curs.execute(update_query)

##------------------------------------------------------------------------------
# curs.execute("SELECT * FROM {}".format("film"))
#
# a = curs.fetchall()
# print(a[0])
#
# for i in a[0]:
#     print(F"type of {i} is {type(i)}")

##------------------------------------------------------------------------------
class Film:
    def __init__(self, film_id, title, description, release_year:str, rate, Lenght:int  )
