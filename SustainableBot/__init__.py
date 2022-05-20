import disnake
from disnake.ext import commands, tasks
import itertools

from .myworld import My_World
from .info import Info

class SustainBot(commands.Bot):
    intents = disnake.Intents.all()

    def __init__(self):
        self.prefix = ["s.", "s ", "S.", "S "]
        super().__init__(command_prefix=self.prefix, intents=SustainBot.intents)
        self.statuss = itertools.cycle(
            [disnake.Activity(type=disnake.ActivityType.watching, name="windmills turn"), disnake.Game(f'{self.prefix[0]}help'), disnake.Game(f'Earth.io')])
        self.remove_command('help')


    @tasks.loop(seconds=60)
    async def change_status(self):
        await self.change_presence(activity=next(self.statuss))

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print(f"{self.user.name} is ready")
