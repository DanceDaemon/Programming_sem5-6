import requests
import json

def get_weather_data(place:str, api_key=''):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ place + '&appid=' + api_key)
    
    if response.status_code.as_integer_ratio == (404):
        print('Wrong city name')
        return None
    if response.status_code.as_integer_ratio == (401):
        print('Invalid API key')
        return None
    
    responseText = json.loads(response.text)
    feels_like = round(responseText['main']['feels_like'] - 273.15, 2)
    if responseText['timezone'] < 0:
        timezone = 'UTC'+str(round(responseText['timezone'] / 3600))
    else:
        timezone = 'UTC+'+str(round(responseText['timezone'] / 3600))
    print({"City": responseText['name'], "Coodinates": responseText['coord'], "Country": responseText['sys']['country'], "Feels_like": feels_like, "Timezone": timezone})

cityName = input('Enter city name: ')
apiKey = 'df1b1a5472b0b607c4143173752ac8a7'

get_weather_data(cityName, apiKey)