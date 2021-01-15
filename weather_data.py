from pprint import pprint
import requests
import json
import urllib.request as utl

def weatherget():
    urls='http://api.openweathermap.org/data/2.5/weather?q=Taipei&units=metric&APPID=d86795050bdc37e209d5cf3fedebfb2d&lang=zh_tw' # your urls here
    r = utl.Request(urls)


    x = utl.urlopen(r)
    weather_data = x.read().decode('utf-8')
    weather_data=weather_data.replace('{','')
    weather_data=weather_data.replace('}','')
    weather_data=weather_data.replace('[','')
    weather_data=weather_data.replace(']','')
    weather_data=weather_data.replace(',','')
    weather_data=weather_data.replace(':','')
    weather_data=weather_data.replace('\""','\"')


    data = [None] * len(weather_data.split('\"'))
    for i in range(len(weather_data.split('\"'))):
        data[i] = weather_data.split('\"',-1)[i]
    #put useful data into variable
    cloud_description = data[12]
    current_temp = data[19]
    feels_like_temp = data[21]
    temp_min = data[23]
    temp_max = data[25]
    humidity = data[29]
    wind_speed = data[34]
    
    return cloud_description,current_temp,feels_like_temp,temp_min,temp_max,humidity,wind_speed



'''
data[]:
    12 = cloud description
    19 = current_temp
    21 = feels_like_temp
    23 = temp_min
    25 = temp_max
    29 = humidity
    34 = wind speed
    
'''


'''
data example
{'base': 'stations',
 'clouds': {'all': 75},
 'cod': 200,
 'coord': {'lat': 25.05, 'lon': 121.53},
 'dt': 1607801937,
 'id': 1668341,
 'main': {'feels_like': 16.78,
          'humidity': 88,
          'pressure': 1015,
          'temp': 17.76,
          'temp_max': 18,
          'temp_min': 17.22},
 'name': 'Taipei',
 'sys###country': 'TW',
         'id': 7949,
         'sunrise': 1607812214,
         'sunset': 1607850367,
         'type': 1},
 'timezone': 28800,
 'visibility': 10000,
 'weather': [{'description': '多雲', 'icon': '04n', 'id': 803, 'main': 'Clouds'}],
 'wind': {'deg': 100, 'speed': 4.1}}
 '''
