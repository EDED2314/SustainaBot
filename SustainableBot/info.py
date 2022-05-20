import disnake
import textwrap
from disnake.ext import commands

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.description = textwrap.dedent((f"""
        **General**
        `{self.bot.prefix[0]}help` - help command
        **View**
        `{self.bot.prefix[0]}view [p]` - views your world/people
        `{self.bot.prefix[0]}delete` - deletes your world
        """))
        self.main_color = (35, 135, 42)


    @commands.command(name="help", aliases=["h"])
    async def help(self, ctx):
        embed = disnake.Embed(title="Help Panel", description=self.description, colour=disnake.Colour.from_rgb(self.main_color[0], self.main_color[1], self.main_color[2]))
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
