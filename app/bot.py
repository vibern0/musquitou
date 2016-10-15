import os
import time
from slackclient import SlackClient
import json
from botfunc import bot_process_message
from dotenv import load_dotenv
load_dotenv(".env")


BOT_ID = os.environ.get("BOT_ID")
BOT_CHANNEL_PRIVATE = os.environ.get("BOT_CHANNEL_PRIVATE")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
AT_BOT = "<@" + str(BOT_ID) + ">"
slack_client = SlackClient(SLACK_BOT_TOKEN)


def handle_command(command, channel):
    response = bot_process_message(command)

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    print(slack_rtm_output)
    output_list = slack_rtm_output

    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and BOT_ID not in output['user'] and BOT_CHANNEL_PRIVATE in output['channel']:
                return output['text'], output['channel']
            elif output and 'text' in output and AT_BOT in output['text']:
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                   output['channel']

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
