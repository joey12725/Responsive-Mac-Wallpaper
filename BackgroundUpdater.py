from datetime import datetime, time
from time import sleep
import requests, json
import os
import subprocess

log = open('log.txt')
CurrentTime = 'day'
CurrentWeather = 'clear sky'
print(log.read())

import requests, json
api_key = #your openweathermap key here
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = #Your city here
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

def in_between(now, start, end):
    if start <= end: #Times before midnight
        return start <= now < end #returns bool
    else: # Times past midnight
        return start <= now or now < end #returns bool

def UpdateStatus():
    if(in_between(datetime.now().time(), time(7), time(17))):
        CurrentTime = 'day'
    elif(in_between(datetime.now().time(), time(17), time(20))):
        CurrentTime = 'sunset'
    elif(in_between(datetime.now().time(), time(20), time(7))):
        CurrentTime = 'night'
    response = requests.get(complete_url)
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # selecting the dict block weather which contains a list length one, the grabbing description from the dictionary conmtained in that list
       CurrentWeather = data['weather'][0]['description']
    else:
       # showing the error message
       print("Error in the HTTP request")
    print(CurrentTime)
    print(CurrentWeather)

    if(CurrentTime == 'day' and CurrentWeather != 'rain'  and CurrentWeather != 'thunderstorm' and CurrentWeather != 'shower rain' and CurrentWeather != 'snow'):
        print("day_dry")
        log = open('log.txt', 'r+')
        OldName = log.read()
        print(OldName)
        os.rename('CurrentWallpaper.gif', OldName)
        log.seek(0)
        log.write('day_dry.gif')
        log.truncate()
        os.rename('day_dry.gif', 'CurrentWallpaper.gif')
    elif(CurrentTime == 'sunset' and CurrentWeather != 'rain'  and CurrentWeather != 'thunderstorm' and CurrentWeather != 'shower rain' and CurrentWeather != 'snow'):
        print("sunset_dry")
        log = open('log.txt', 'r+')
        OldName = log.read()
        print(OldName)
        os.rename('CurrentWallpaper.gif', OldName)
        log.seek(0)
        log.write('sunset_dry.gif')
        log.truncate()
        os.rename('sunset_dry.gif', 'CurrentWallpaper.gif')
    elif(CurrentTime == 'night' and CurrentWeather != 'rain'  and CurrentWeather != 'thunderstorm' and CurrentWeather != 'shower rain' and CurrentWeather != 'snow'):
        print("night_dry")
        log = open('log.txt', 'r+')
        OldName = log.read()
        print(OldName)
        os.rename('CurrentWallpaper.gif', OldName)
        log.seek(0)
        log.write('night_dry.gif')
        log.truncate()
        os.rename('night_dry.gif', 'CurrentWallpaper.gif')
    elif(CurrentWeather == 'rain' or CurrentWeather == 'thunderstorm' or CurrentWeather == 'shower rain' or CurrentWeather == 'snow'):
        if(CurrentTime == 'day'):
            print("day_rain")
            log = open('log.txt', 'r+')
            OldName = log.read()
            print(OldName)
            os.rename('CurrentWallpaper.gif', OldName)
            log.seek(0)
            log.write('day_rain.gif')
            log.truncate()
            os.rename('day_rain.gif', 'CurrentWallpaper.gif')
        if(CurrentTime == 'sunset'):
            print("sunset_rain")
            log = open('log.txt', 'r+')
            OldName = log.read()
            print(OldName)
            os.rename('CurrentWallpaper.gif', OldName)
            log.seek(0)
            log.write('sunset_rain.gif')
            log.truncate()
            os.rename('sunset_rain.gif', 'CurrentWallpaper.gif')
        if(CurrentTime=='night'):
            print("night_rain")
            log = open('log.txt', 'r+')
            OldName = log.read()
            print(OldName)
            os.rename('CurrentWallpaper.gif', OldName)
            log.seek(0)
            log.write('night_rain.gif')
            log.truncate()
            os.rename('night_rain.gif', 'CurrentWallpaper.gif')
    else:
        print('error selecting time or weather condition')
while True:
    UpdateStatus()
    sleep(900)
