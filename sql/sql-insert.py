# import required libraries
import sqlite3
import random


# connect to the database
with sqlite3.connect('newnum.db') as connection:

	# create a cursor object
	c = connection.cursor()

	# create a list of 100 random integers
	data = [(random.randint(0, 100),) for i in range(0, 100)]

	# if table exists, drop the table
	c.execute("DROP TABLE IF EXISTS random_integers")

	# execute query to add random integers to a table
	c.execute("CREATE TABLE random_integers (numbers INT)")

	# execute query to add random integers to a table
	c.executemany("INSERT INTO random_integers VALUES(?)", data)

