import discord
import requests
import json
import time

TOKEN = '' # <<<<<<<<<YOUR TOKEN>>>>>>>>>>>>>

class FortUpdate(discord.Client):
    def __init__(self,intents):
        super().__init__(intents=intents)

    async def on_ready(self): 
        print(f'{self.user} has connected to Discord!')
        await self.send_update()

    async def send_update(self):
        self.news_channel = super().get_channel(1068125978452303914)
        while True:
            # Get the latest update from the Fort API
            with open("latest.txt","r+") as f:
                try:
                    latest_update = f.read()
                except:
                    pass
            url = 'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/version'
            r = requests.get(url)
            data = json.loads(r.text)
            # Send the message to the channel
            if data['version'] != latest_update:
                latest_update = data['version']
                with open("latest.txt",'r+') as f:
                    f.truncate(0)
                    f.write(latest_update)
                await self.news_channel.send('A new Fortnite update is available!')
            else:
                try:
                    await self.news_channel.send("Fortnite is Up-To-Date!! 5 sec elapsed")
                except Exception as e:
                    print(e)
            time.sleep(10) #put a sleep time to mention how many seconds a time the script will check for an update

intents = discord.Intents.default()
intents.message_content = True
   
client = FortUpdate(intents=intents)

client.run(TOKEN)
