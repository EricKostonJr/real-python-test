import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()



	sql = {
		'Honda': "SELECT count(order_date) FROM orders WHERE make = 'Honda'",
		'Ford': "SELECT count(order_date) FROM orders WHERE make = 'Ford'",
		'Focus': "SELECT count(order_date) FROM orders WHERE model = 'Focus'",
		'F150': "SELECT count(order_date) FROM orders WHERE model = 'F150'",
		'Explorer': "SELECT count(order_date) FROM orders WHERE model = 'Explorer'",
		'Accord': "SELECT count(order_date) FROM orders WHERE model = 'Accord'",
		'Civic': "SELECT count(order_date) FROM orders WHERE model = 'Civic'"
		}

	for keys, values in sql.items():

		c.execute(values)

		result = c.fetchone()

		print(keys + ': ' + str(result[0]))