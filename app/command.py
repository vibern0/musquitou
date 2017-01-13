

class Command:
    def __init__(self, api):
        self.__api = api

    def process(self, command):

        response = 'I cant understand!'
        if command.startswith('weather'):

            params = command.split(' ')
            if len(params) < 2:
                return 'You need to say the city name'

            if 'tomorrow' in command:
                response = self.__api.weather.tomorrow(params[1])

            elif '5days' in command:
                response = self.__api.weather.five_days(params[1])

            else:
                response = self.__api.weather.today(params[1])

        return response
