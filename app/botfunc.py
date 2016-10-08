import requests
import json
import os
import pprint
from random import randint
from dotenv import load_dotenv
load_dotenv(".env")


headers = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key":os.environ.get("ZOMATO_USER_KEY")}


def bot_process_message(command):
    response = 'I cant understand!'
    if command.startswith('hi'):
        response = 'hi friend'

    return response
