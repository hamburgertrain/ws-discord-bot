# ws-discord-bot
 Discord bot for Raspberry Pi weather station.
 Responds to '!temp' with temperature and humidity readings.

## Getting Started

### Installing Dependencies

https://github.com/Rapptz/discord.py
https://github.com/adafruit/Adafruit_Python_DHT

#### Install python3 and python3-pip
```
sudo apt-get install python3 python3-pip
```

#### Install pip packages for Discord and Adafruit DHT
```
sudo pip3 install Adafruit_DHT
```
```
python3 -m pip install -U discord.py
```

### Config and Running

#### Insert your discord bot API key
In bot.py, change bot_token to your Discord bot token
```python
bot_token = 'YOUR_DISCORD_BOT_TOKEN_HERE'
```

#### Run it!
cd to root directory of repo
```
. start.sh
```

or

```
python3 bot.py
```