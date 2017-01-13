import requests


class Weather:
    def __init__(self, api):
        self.__api = api

    def call(self, city, days):
        r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=' +
                         city + '&cnt=' + str(days) +
                         '&APPID=' + str(self.__api.WEATHER_API_TOKEN))
        answer = r.json()
        return answer

    def today(self, city):
        answer = self.call(city, 1)
        response = answer['list'][0]['weather'][0]['main'] + ', ' + \
                   answer['list'][0]['weather'][0]['description']
        return response

    def tomorrow(self, city):
        answer = self.call(city, 2)
        response = answer['list'][1]['weather'][0]['main'] + ', ' + \
                   answer['list'][1]['weather'][0]['description']
        return response

    def five_days(self, city):
        answer = self.call(city, 5)
        response = ''
        for x in range(0, 5):
            response += 'Day ' + str(x + 1) + ' ' + \
                        answer['list'][x]['weather'][0]['main'] + ', ' + \
                        answer['list'][x]['weather'][0]['description'] + '\n'
        return response
