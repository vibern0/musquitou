# musquitou
A musquitou can be either :+1: or :-1:

### Description:
This is a bot for [Slack][slack]. This bot can help you in public channels or in private (direct message). He works in different ways. In public channels you need to refer to him like *"@musquitou-bot (message)"* but in private, just talk to him, and he will answer to everythin.

### Table of contents:
For now, this bot is made only to help get the weather. In the future we are thinking about add more features.

### Installation:
First, generate the virtual environment by doing<br/>
`virtualenv musquitoubot`<br/>
and activate with<br/>
`source musquitoubot/bin/activate`
<br/><br/>
Then go to *app* folder and do<br/>
`pip install -r requirements`<br/>
(maybe you need to use 'sudo' in unix environment)
<br/><br/>
Now it's needed a `.env` file with some variables.<br/>
`BOT_ID = <>` (you can find [here](https://api.slack.com/methods/users.list/test) by selecting your team and do 'Test Method')<br/>
`BOT_CHANNEL_GENERAL = <>` (same has above, but [here](https://api.slack.com/methods/channels.list/test))<br/>
`SLACK_BOT_TOKEN = <>` it will be available when bot is created<br/>
`WEATHER_API_TOKEN = <>` (register yourself and get a token [here](https://openweathermap.org/api))<br/>
<br/>
Now it's ready to go `python main.py`
### Usage:
To get the weather just write `weather <city> <days (optional) >`

### Contributing:
We dont have any limits to this bot, so, if you come with an idea, something you think it's useful, just open an issue talking about it, or *fork* the project, make the changes and *pull request*. 

### Credits:
[obernardveira][obernardveirap]<br/>
[InesPessoa][inespessoap]

### License:
GNUv3

[slack]: <https://slack.com/>
[obernardveirap]: <https://github.com/obernardovieira>
[inespessoap]: <https://github.com/InesPessoa>
