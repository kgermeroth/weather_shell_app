import os, requests

api_key = os.environ['ACCUWEATHER_API_KEY']

def get_location_key():
	"""Takes zipcode, queries Accuweather API and returns location key"""

	zipcode = '94607'

	# url = f'http://dataservice.accuweather.com/locations/v1/search?apikey={api_key}&q={zipcode}'

	# response = requests.get(url)

	# data = response.json()

	# location_key = data[0]['Key']

	location_key = '39601_PC'

	return location_key