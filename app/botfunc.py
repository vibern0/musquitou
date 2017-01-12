import os
import requests
from dotenv import load_dotenv
load_dotenv(".env")

WEATHER_API_TOKEN = os.environ.get("WEATHER_API_TOKEN")


def bot_process_message(command):
    response = 'I cant understand!'
    if command.startswith('hi'):
        response = 'hi friend'

    elif command.startswith('weather'):
        params = command.split(' ')
        days = '1';
        if len(params) > 2:
            days = params[2]
        elif len(params) < 2:
            return 'You need to say the city name'
        r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q='
                         + params[1] + '&cnt=' + days + '&APPID=' + str(WEATHER_API_TOKEN))
        ans = r.json()
        if int(days) > 1:
            response = ''
            for x in range(0, int(days)):
                response += 'Day ' + str(x + 1) + ' ' +\
                            ans['list'][x]['weather'][0]['main'] + ', ' +\
                            ans['list'][x]['weather'][0]['description'] + '\n'
        else:
            response = ans['list'][0]['weather'][0]['main'] + ', ' +\
                       ans['list'][0]['weather'][0]['description']

    return response
