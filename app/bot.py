import os
import time
from slackclient import SlackClient
from botfunc import bot_process_message
from dotenv import load_dotenv

load_dotenv(".env")

BOT_ID = os.environ.get("BOT_ID")
BOT_CHANNEL_GENERAL = os.environ.get("BOT_CHANNEL_GENERAL")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
AT_BOT = "<@" + str(BOT_ID) + ">"
slack_client = SlackClient(SLACK_BOT_TOKEN)

public_channels_list = [BOT_CHANNEL_GENERAL]


def handle_command(command, channel):
    response = bot_process_message(command)

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    print(slack_rtm_output)
    output_list = slack_rtm_output

    if len(output_list) < 1:
        return None, None

    for output in output_list:

        if 'text' not in output:
            return None, None

        if BOT_ID in output['user']:
            return None, None

        if AT_BOT in output['text']:
            return output['text'].split(AT_BOT)[1].strip().lower(), \
                   output['channel']
        else:
            for channel in public_channels_list:
                if channel not in output['channel']:
                    return output['text'], output['channel']

    return None, None


def run_bot():
    if slack_client.rtm_connect():
        print("bot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(1)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
