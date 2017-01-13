import time


class Input:
    def __init__(self, api):
        self.__api = api

    def read(self):
        while True:
            command, channel = self.parse(self.__api.slack_client.rtm_read())
            if command and channel:
                self.__api.answer(command, channel)
            time.sleep(1)

    def parse(self, output_list):
        print(output_list)
        if len(output_list) < 1:
            return None, None

        for output in output_list:

            if 'text' not in output:
                return None, None

            if self.__api.BOT_ID in output['user']:
                return None, None

            if self.__api.AT_BOT in output['text']:
                return output['text'].split(self.__api.AT_BOT)[1].strip().lower(), \
                       output['channel']
            else:
                for channel in self.__api.public_channels_list:
                    if channel not in output['channel']:
                        return output['text'], output['channel']

        return None, None
