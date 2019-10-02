# Weather App

## Table of Contents

* [Summary](#summary)
* [Tech Stack](#techstack)
* [Features](#features)
* [Installation](#installation)
* [Getting Your API Key](#apikey)


## <a name="summary"></a>Summary
This simple to install tool allows you to get the weather forecast for any zipcode in the United States directly from the command line. Weather forecast includes hourly forecasts for the next 12 hours, including temperature, chance of precipitation, and general conditions. There is also daily forecasts for the next 5 days, with low and high temperatures, chance of precipitation, and general conditions.</br>

Please note that an AccuWeather API Key is needed for this tool. This is free for fewer than 50 API calls per day.  

## <a name="techstack"></a>Tech Stack
__Tech Stack:__ Python

## <a name="features"></a>
To get the weather forecast for your default zipcode:
```
$ weather
```
![default](/static/defaultzip.png)

To get the weather forecast for a different zipcode:
```
$ weather zipcode
```
![zipcode](/static/withzip.png)

## <a name="installation"></a>Installation

#### Requirements:
- Python 3.6.8
- [AccuWeather API Key](#apikey)

To install this tool on your machine, please follow the below steps:

Clone repository into a folder of your choice:
```
$ git clone https://github.com/kgermeroth/weather_shell_app
```

Choose a directory in your path for the remainder of installation. 

If you are unsure of this step, it is recommended to create a 'bin' directory in your ~ (home) directory and then ensure it is in your path. 
Learn how to add a directory to your path <a href="https://www.techrepublic.com/article/how-to-add-directories-to-your-path-in-linux/">here</a>. 

While in the directory where you cloned the project, run the following code, replacing the capitalized variables with the appropriate arguments:
```
$ ./install.sh INSTALL_DIRECTORY API_KEY DEFAULT_ZIPCODE
```

That's it! Now you have the weather at your fingertips regardless of what directory you are in. 

For weather for your default zipcode:
```
$ weather
```

For weather for a different zipcode:
```
$ weather ZIPCODE
```

## <a name="apikey"></a>Getting Your AccuWeather API Key
Register for an AccuWeather account <a href="https://developer.accuweather.com/user/register">here</a>.</br>

Navigate to 'MY APPS' and create a new app:
![createapp](/static/createapp.png)

Once your app is approved, select your app name. Your API Key will be in there!
![getkey](/static/getkey.png)








