# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import datetime
from SimpleWeatherApp import README, config

config.api_key = '159324399fe40a146937030dc0d50c8a' # OpenWeather API key
config.openweather_url = 'http://api.openweathermap.org/data/2.5/weather?'

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    location = input('Enter location: ')
    if len(location) < 1: break

    parameter = dict()
    parameter['q'] = location
    parameter['APPID'] = config.api_key
    url = config.openweather_url + urllib.parse.urlencode(parameter)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None

    print('Weather in', location)
    name = js['name']
    country = js['sys']['country']
    print('===', name, ',', country, '===')

    # Date and Time
    currentDT = datetime.datetime.now()
    date = currentDT.strftime("%m/%d/%Y")
    time = currentDT.strftime("%I:%M %p")
    day = currentDT.strftime("%a")
    print("===", day, date, time, "===")

    # Temperature
    temp = js['main']['temp']
    celcius = float(temp) - 273.15 # Kelvin to Celcius
    print('Temperature:', '{:.1f}'.format(celcius), 'C')

    # Weather
    weather = js['weather'][0]['main']
    weather_description = js['weather'][0]['description']
    print('Weather: ', weather)
    print('Description: ', weather_description)

    # Wind speed
    wind_speed = js['wind']['speed']
    print('Wind:', wind_speed, 'm/s')
    # break

# print('======================')
# print(README.__author__)
# print(README.__copyright__)
# print(README.__email__)