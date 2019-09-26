#!/usr/bin/env python3

import os, requests, sys
from datetime import datetime


api_key = os.environ['ACCUWEATHER_API_KEY']

def get_location_key():
	"""Takes zipcode, queries Accuweather API and returns location key"""

	zipcode = str(sys.argv[1])

	# validate user entry for zipcode
	if len(zipcode) != 5 or not zipcode.isnumeric():
		print(f'"{zipcode}"" is not a valid zipcode.')
		print('Please enter 5 digit zipcode')

		return 

	else:

		url = f'http://dataservice.accuweather.com/locations/v1/search?apikey={api_key}&q={zipcode}'

		response = requests.get(url)

		data = response.json()

		location_key = data[0]['Key']

		city = data[0]['LocalizedName'] + ', ' + data[0]['AdministrativeArea']['ID']

		return (location_key, city)


def get_hourly_forecast(location_key, city):
	"""Gets next 12 hours of hourly forecast and prints to terminal"""

	url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}?apikey={api_key}'

	response = requests.get(url)

	data = response.json()

	print(f'\nWEATHER FORECAST FOR: {city}\n')
	print('Today\'s Hourly Forecast:')

	for item in data:
		short_date = item['DateTime'][:-6]
		datetime_object = datetime.strptime(short_date, '%Y-%m-%dT%H:%M:%S')

		time = datetime_object.strftime('%I %p')

		temperature = str(int(item['Temperature']['Value'])) + item['Temperature']['Unit']

		precipitation = str(item['PrecipitationProbability']) + '%'

		condition = item['IconPhrase']

		print(f'\t{time}:\t{temperature}\tPrecip:\t{precipitation}\tConditions: {condition}')


def get_daily_forecast(location_key):
	"""Gets 5 day forecast and prints to terminal"""

	url = f'http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}?apikey={api_key}&details=true'

	response = requests.get(url)

	data = response.json()

	print('\nDaily Forecast:')

	for forecast in data['DailyForecasts']:

		short_date = forecast['Date'][:10]
		datetime_object = datetime.strptime(short_date, '%Y-%m-%d')
		date = datetime_object.strftime('%a, %b %d')

		low_temp = str(int(forecast['Temperature']['Minimum']['Value'])) + str(forecast['Temperature']['Minimum']['Unit'])
		high_temp = str((int(forecast['Temperature']['Maximum']['Value']))) + str(forecast['Temperature']['Maximum']['Unit'])

		precipitation = str(forecast['Day']['PrecipitationProbability']) + '%'

		condition = forecast['Day']['IconPhrase']


		print(f'\t{date}: \tLow: {low_temp}\tHigh: {high_temp}\tPrecip: {precipitation}\tConditions: {condition}')


def display_forecast():
	"""Runs forecast app"""

	result = get_location_key()

	# only run all functions if the first did not return None
	if result:
		location_key, city = result

		get_hourly_forecast(location_key, city)
		get_daily_forecast(location_key)

		print('\nData courtesy of AccuWeather')

display_forecast()


