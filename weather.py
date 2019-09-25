#!/usr/bin/env python3

import os, requests, sys

api_key = os.environ['ACCUWEATHER_API_KEY']

def get_location_key():
	"""Takes zipcode, queries Accuweather API and returns location key"""

	zipcode = str(sys.argv[1])

	# validate user entry for zipcode
	if len(zipcode) != 5 or not zipcode.isnumeric():
		print(f'"{zipcode}"" is not a valid zipcode.')
		print('Please enter 5 digit zipcode')

	else:

		# url = f'http://dataservice.accuweather.com/locations/v1/search?apikey={api_key}&q={zipcode}'

		# response = requests.get(url)

		# data = response.json()

		# location_key = data[0]['Key']

		location_key = '39601_PC'

		print(location_key)

		return location_key


def get_hourly_forecast(location_key):
	"""Gets next 12 hours of hourly forecast and prints to terminal"""

	pass

get_location_key()