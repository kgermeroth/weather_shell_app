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

		# url = f'http://dataservice.accuweather.com/locations/v1/search?apikey={api_key}&q={zipcode}'

		# response = requests.get(url)

		# data = response.json()

		data = [{'Version': 1, 'Key': '5705_PC', 'Type': 'PostalCode', 'Rank': 45, 'LocalizedName': 'Rochester', 'EnglishName': 'Rochester', 'PrimaryPostalCode': '14623', 
				'Region': {'ID': 'NAM', 'LocalizedName': 'North America', 'EnglishName': 'North America'}, 'Country': {'ID': 'US', 'LocalizedName': 'United States', 'EnglishName': 'United States'}, 
				'AdministrativeArea': {'ID': 'NY', 'LocalizedName': 'New York', 'EnglishName': 'New York', 'Level': 1, 'LocalizedType': 'State', 'EnglishType': 'State', 'CountryID': 'US'}, 
				'TimeZone': {'Code': 'EDT', 'Name': 'America/New_York', 'GmtOffset': -4.0, 'IsDaylightSaving': True, 'NextOffsetChange': '2019-11-03T06:00:00Z'}, 
				'GeoPosition': {'Latitude': 43.088, 'Longitude': -77.644, 'Elevation': {'Metric': {'Value': 164.0, 'Unit': 'm', 'UnitType': 5}, 
				'Imperial': {'Value': 537.0, 'Unit': 'ft', 'UnitType': 0}}}, 'IsAlias': False, 'ParentCity': {'Key': '329674', 'LocalizedName': 'Rochester', 'EnglishName': 'Rochester'}, 
				'SupplementalAdminAreas': [{'Level': 2, 'LocalizedName': 'Monroe', 'EnglishName': 'Monroe'}], 'DataSets': ['Alerts', 'DailyAirQualityForecast', 'DailyPollenForecast', 'ForecastConfidence', 'MinuteCast', 'Radar']}]


		location_key = data[0]['Key']

		city = data[0]['LocalizedName'] + ', ' + data[0]['AdministrativeArea']['ID']

		return (location_key, city)


def get_hourly_forecast(location_key, city):
	"""Gets next 12 hours of hourly forecast and prints to terminal"""

	# url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}?apikey={api_key}'

	# response = requests.get(url)

	# data = response.json()

	data = [{'DateTime': '2019-09-25T20:00:00-04:00', 'EpochDateTime': 1569456000, 'WeatherIcon': 35, 'IconPhrase': 'Partly cloudy', 'HasPrecipitation': False, 'IsDaylight': False, 
			'Temperature': {'Value': 72.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 0, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=1&hbhhour=20&lang=en-us', 
			'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=1&hbhhour=20&lang=en-us'}, 
			{'DateTime': '2019-09-25T21:00:00-04:00', 'EpochDateTime': 1569459600, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 69.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 0, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=1&hbhhour=21&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=1&hbhhour=21&lang=en-us'}, {'DateTime': '2019-09-25T22:00:00-04:00', 'EpochDateTime': 1569463200, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 67.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 0, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=1&hbhhour=22&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=1&hbhhour=22&lang=en-us'}, {'DateTime': '2019-09-25T23:00:00-04:00', 'EpochDateTime': 1569466800, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 66.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 0, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=1&hbhhour=23&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=1&hbhhour=23&lang=en-us'}, {'DateTime': '2019-09-26T00:00:00-04:00', 'EpochDateTime': 1569470400, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 65.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 0, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=0&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=0&lang=en-us'}, {'DateTime': '2019-09-26T01:00:00-04:00', 'EpochDateTime': 1569474000, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 64.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 2, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=1&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=1&lang=en-us'}, {'DateTime': '2019-09-26T02:00:00-04:00', 'EpochDateTime': 1569477600, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 64.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 7, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=2&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=2&lang=en-us'}, {'DateTime': '2019-09-26T03:00:00-04:00', 'EpochDateTime': 1569481200, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 63.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 7, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=3&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=3&lang=en-us'}, {'DateTime': '2019-09-26T04:00:00-04:00', 'EpochDateTime': 1569484800, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 63.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 6, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=4&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=4&lang=en-us'}, {'DateTime': '2019-09-26T05:00:00-04:00', 'EpochDateTime': 1569488400, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 62.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 5, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=5&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=5&lang=en-us'}, {'DateTime': '2019-09-26T06:00:00-04:00', 'EpochDateTime': 1569492000, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 62.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 5, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=6&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=6&lang=en-us'}, {'DateTime': '2019-09-26T07:00:00-04:00', 'EpochDateTime': 1569495600, 'WeatherIcon': 36, 'IconPhrase': 'Intermittent clouds', 'HasPrecipitation': False, 'IsDaylight': False, 'Temperature': {'Value': 61.0, 'Unit': 'F', 'UnitType': 18}, 'PrecipitationProbability': 8, 'MobileLink': 'http://m.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=7&lang=en-us', 'Link': 'http://www.accuweather.com/en/us/pittsburgh-pa/15219/hourly-weather-forecast/6002_pc?day=2&hbhhour=7&lang=en-us'}]

	print(f'\nWEATHER FORECAST FOR: {city}\n')
	print('Hourly Forecast:')

	for item in data:
		short_date = item['DateTime'][:-6]
		datetime_object = datetime.strptime(short_date, '%Y-%m-%dT%H:%M:%S')

		time = datetime_object.strftime('%I %p')

		temperature = str(int(item['Temperature']['Value'])) + item['Temperature']['Unit']

		precipitation = str(item['PrecipitationProbability'] * 10) + '%'

		condition = item['IconPhrase']

		print(f'\t{time}:\t{temperature}\tPrecip:\t{precipitation}\tConditions: {condition}')


def display_forecast():
	"""Runs forecast app"""

	result = get_location_key()

	# only run all functions if the first did not return None
	if result:
		location_key, city = result

		get_hourly_forecast(location_key, city)


display_forecast()
