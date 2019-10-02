#!/usr/bin/env bash

set -e

if [ $# -ne 3 ]; then
	echo invalid usage:
	echo ./install.sh DIRECTORY_PATH API_KEY ZIPCODE 
	exit
fi

directory="$1"
api_key="$2"
zipcode="$3"

install_script=$(realpath $0)
install_directory=$(dirname $install_script)

weather_path=${install_directory}/weather.py

cd ${directory}

ln -s ${weather_path} weather

mkdir -p ~/.config/weather_app
touch ~/.config/weather_app/config.json

cat << EOF > ~/.config/weather_app/config.json
{
	"ACCUWEATHER_API_KEY" : "${api_key}",
	"DEFAULT_ZIPCODE" : "${zipcode}"
}
EOF

pip3 install -r ${install_directory}/requirements.txt

