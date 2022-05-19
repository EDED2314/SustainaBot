import disnake
import textwrap
from disnake.ext import commands

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.description = textwrap.dedent((f"""
        **General**
        `{self.bot.prefix[0]}help` - help command
        """))


    @commands.command()
    async def help(self, ctx):
        embed = disnake.Embed(title="Help Panel", description=self.description, color=disnake.Color.blurple())
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
