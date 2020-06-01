# import required libraries
import sqlite3


# create a prompt for the user
prompt = """What would you like to do?\n
You can say:
'AVERAGE'
'MAXIMUM'
'MINIMUM'
'SUM' or
'EXIT'\n"""


# loop through for user input
while True:
	# save user input
	user = input(prompt)

	if user == 'AVERAGE':
		query = 'AVG'
	elif user == 'MAXIMUM':
		query = 'MAX'
	elif user == 'MINIMUM':
		query = 'MIN'
	elif user == 'SUM':
		query = 'SUM'
	elif user == 'EXIT':
		break
	else:
		print('Your response was invalid. Please pick again.\n')
		continue




	# connect to the database
	with sqlite3.connect('newnum.db') as connection:

		# create cursor object
		c = connection.cursor()

		# build query
		c.execute("SELECT {}(numbers) FROM random_integers".format(query))

		response = c.fetchone()

		# print the output
		print("{}: {}\n\n".format(user, response[0]))