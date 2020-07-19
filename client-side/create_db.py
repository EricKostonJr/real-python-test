# Create a SQLite3 database and table


import sqlite3

with sqlite3.connect('movies.db') as connection:
	c = connection.cursor()


	# create a table
	c.execute("""CREATE TABLE new_movies
						(title TEXT, year INT, votes TEXT,
						release_date TEXT, rating INT, metascore INT)""")