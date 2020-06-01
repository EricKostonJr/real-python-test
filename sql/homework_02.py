# homework_02

import sqlite3


with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()

	data = [
		('Ford', 'Focus', 14),
		('Ford', 'F150', 10),
		('Ford', 'Explorer', 20),
		('Honda', 'Civic', 45),
		('Honda', 'Accord', 32)
	]

	c.executemany("INSERT INTO inventory(Make, Model, Quantity) values (?, ?, ?)", data)

