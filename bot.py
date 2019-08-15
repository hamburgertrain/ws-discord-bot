# Discord Weather Bot
# Copyright (C) 2019  Tyler Bialoblocki
# tylerbialoblocki@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import discord
import Adafruit_DHT
import sys

# Prefix for commands
command_prefix = '!'

# Discord bot token
bot_token = 'YOUR_DISCORD_BOT_TOKEN_HERE'

# GPIO pin which sensor is hooked up to
gpio_pin = 4

# Type of sensor: Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, Adafruit_DHT.AM2302
sensor_type = Adafruit_DHT.AM2302

async def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(sensor_type, gpio_pin)

    # Comment out line for celsius
    temperature = temperature * 9/5.0 + 32

    if humidity is not None and temperature is not None:
        return 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
    else:
        return 'There was an error reading the sensor.'

class WeatherClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == command_prefix + 'temp':
            result = await read_sensor()
            await message.channel.send(result)

client = WeatherClient()
client.run(bot_token)
