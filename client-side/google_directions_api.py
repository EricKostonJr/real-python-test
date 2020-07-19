import requests, json, os



key = os.environ['google_api_key']
url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Central+Park&destination=Times+Square&mode=walking&key={}'.format(key)

data = requests.get(url)
binary = data.content
output = json.loads(str(binary, 'utf-8'))
print(output['status'])

for route in output['routes']:
	for leg in route['legs']:
		print(leg['start_address'])
		print(leg['end_address'])