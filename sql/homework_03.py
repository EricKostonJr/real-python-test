import sqlite3


with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()

	c.execute("""UPDATE inventory SET Quantity = 40
					WHERE Model='F150'""")

	c.execute("""UPDATE inventory SET Quantity = 30
					WHERE Model='Civic'""")