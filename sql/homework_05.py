import sqlite3

with sqlite3.connect('cars.db') as connection:
    # create cursor object
    c = connection.cursor()

    # define data object
    orders = [
            ('Honda', 'Accord', '2020-01-01'),
            ('Honda', 'Accord', '2019-01-01'),
            ('Honda', 'Accord', '2018-01-01'),
            ('Honda', 'Civic', '2020-01-01'),
            ('Honda', 'Civic', '2019-01-01'),
            ('Honda', 'Civic', '2018-01-01'),
            ('Ford', 'Explorer', '2020-01-01'),
            ('Ford', 'Explorer', '2019-01-01'),
            ('Ford', 'Explorer', '2018-01-01'),
            ('Ford', 'F150', '2020-01-01'),
            ('Ford', 'F150', '2019-01-01'),
            ('Ford', 'F150', '2018-01-01'),
            ('Ford', 'Focus', '2020-01-01'),
            ('Ford', 'Focus', '2019-01-01'),
            ('Ford', 'Focus', '2018-01-01')
        ]

    # create the order table
    c.execute("""CREATE TABLE orders
                (make TEXT, model TEXT, order_date)
              """)

	# insert data
    c.executemany("""INSERT INTO orders VALUES (?, ?, ?)""", orders)