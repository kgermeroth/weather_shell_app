#!/usr/bin/env bash

echo Enter your AccuWeather API Key:
read apiKey
echo Enter default zipcode (ENTER to leave blank)
read zipcode

mkdir -p ~/.config/weather_app
touch ~/.config/weather_app/config.json

cat << EOF > ~/.config/weather_app/config.json
{
	"ACCUWEATHER_API_KEY" : "${apiKey}",
	"DEFAULT_ZIPCODE" : "${zipcode}"
}
EOF

pip3 install -r requirements.txt

