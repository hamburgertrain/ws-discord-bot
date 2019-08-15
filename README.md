# ws-discord-bot
 Discord bot for Raspberry Pi weather station.

## Getting Started

### Installing Dependencies

#### Install python3 and python3-pip
```
sudo apt-get install python3 python3-pip
```

#### Install pip packages for discord and Adafruit DHT
```
sudo pip3 install Adafruit_DHT
```
```
python3 -m pip install -U discord.py
```

### Config and Running

#### Insert your discord bot API key
In bot.py, change bot_token to your discord bot token
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