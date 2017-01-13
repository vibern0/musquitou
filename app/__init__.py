import os
from slackclient import SlackClient
from dotenv import load_dotenv
from input import Input
from command import Command
from weather import Weather


class Musquitou:
    def __init__(self):
        load_dotenv(".env")
        #
        BOT_CHANNEL_GENERAL = os.environ.get("BOT_CHANNEL_GENERAL")
        SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
        #
        self.BOT_ID = os.environ.get("BOT_ID")
        self.AT_BOT = "<@" + str(self.BOT_ID) + ">"
        self.WEATHER_API_TOKEN = os.environ.get("WEATHER_API_TOKEN")
        self.slack_client = SlackClient(SLACK_BOT_TOKEN)
        self.public_channels_list = [BOT_CHANNEL_GENERAL]
        self.input = Input(self)
        self.command = Command(self)
        self.weather = Weather(self)
        #
        if self.slack_client.rtm_connect():
            print("Bot connected and running!")
            self.input.read()
        else:
            print("Connection failed. Invalid Slack token or bot ID?")

    def answer(self, command, channel):
        response = self.command.process(command)
        self.slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
