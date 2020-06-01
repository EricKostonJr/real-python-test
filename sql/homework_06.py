import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT inventory.Make, inventory.Model,
                    orders.order_date FROM inventory, orders
                    WHERE inventory.Model = orders.model""")

    rows = c.fetchall()

    for r in rows:
        print('Make: ' + r[0])
        print('Model: ' + r[1])
        print('Order Date: ' + r[2])
        print('')