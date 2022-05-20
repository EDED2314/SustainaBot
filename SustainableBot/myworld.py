import textwrap
import disnake
from disnake.ext import commands
import pickle
from .World import World
import os


class My_World(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.main_color = (35, 135, 42)

    @commands.command(name="view", aliases=["v"])
    async def view_my_world(self, ctx: commands.Context, mode=None):
        if mode is None:
            world = await self.load_world(ctx)
            description = textwrap.dedent(f"""
            ♥Your world's overall **health**🌎 - `{world.health}`
            👨Your world's **population**👩 - `{world.humans}`
            
            🚗Amount of **MSG-CO2**🚗 - `{world.co2}`
            🐖Amount of avaliable **food**🌲 - `{world.aval_food}`
            💦Amount of avaliable **water**🌊 - `{world.aval_water}`
            
            👣Your **MSG foodtprint**🌱 - `{world.msg_co2}`
            
            💨Amount of **Windmills**{"<:windmill:976908531221532702>"} - `{world.windmills}`
            ☀Amount of **Solar Panels**{"<:solarpanel:976985805815943229>"} - `{world.solarpanels}`
            💧Amonut of **Hydraulic Plants**🏭 - `{world.hydrualicplants}`
            ⚛Amount of **Nuclear Reactors**{"<:reactor:976987157354922044>"} - `{world.nuclearreactors}`
            """)
            embed = disnake.Embed(
                colour=disnake.Colour.from_rgb(self.main_color[0], self.main_color[1], self.main_color[2]),
                title=f"{ctx.author.name}'s mini world!", description=description)
            ig_health = int(round(world.health, -1))
            embed.set_image(file=disnake.File(f"static/images/earths/{ig_health}earth.jpg"))
            embed.set_footer(icon_url=ctx.author.avatar.url)

            await ctx.send(embed=embed)
            return
        elif mode == "people" or mode == "p":
            world = await self.load_world(ctx)
            humans = world.get_humans()
            description = """"""
            for human in humans:
                formatted_str = ""
                for key, val in human.items():
                    formatted_str += f"{key} - `{val}`\n"
                formatted_str += "\n"
                description += formatted_str
            embed = disnake.Embed(
                colour=disnake.Colour.from_rgb(self.main_color[0], self.main_color[1], self.main_color[2]),
                title=f"{ctx.author.name}'s mini world's people!",
                description=description
            )
            embed.set_footer(icon_url=ctx.author.avatar.url)
            await ctx.send(embed=embed)
            await self.write_data(ctx, world)
            return

    @commands.command(name="delete", aliases=['d'])
    async def delete_my_world(self, ctx):
        try:
            os.remove(f"worlds/{ctx.author.id}.pkl")
            await ctx.send("Deleted your world 😢")
            return
        except FileNotFoundError:
            await ctx.send("Deleted your **non existing** world 😢")
            return

    @commands.Cog.listener()
    async def on_message(self, msg: disnake.Message):
        if msg.author == self.bot.user:
            return
        for prefix in self.bot.prefix:
            if prefix in msg.content[0:3]:
                return
        world = await self.load_world(msg)
        world.add_human()
        world.msg_co2 += 1
        world.health = round((world.aval_water + world.aval_food)/2 - world.co2, 2)
        await self.write_data(msg, world)

    @staticmethod
    async def load_world(ctx) -> World:
        try:
            with open(f'worlds/{ctx.author.id}.pkl', 'rb') as inp:
                world = pickle.load(inp)
        except FileNotFoundError:
            with open(f'worlds/{ctx.author.id}.pkl', 'wb') as outp:
                world = World()
                await ctx.channel.send("Since this is your first time here, here is a new world for you!")
                pickle.dump(world, outp, -1)
        return world


    @staticmethod
    async def write_data(ctx, world):
        with open(f'worlds/{ctx.author.id}.pkl', 'wb') as outp:
            pickle.dump(world, outp, -1)
        return

    @staticmethod
    async def save_world(ctx: commands.Context, world: World):
        with open(f'worlds/{ctx.author.id}.pkl', 'wb') as outp:
            pickle.dump(world, outp, -1)
        return

    async def cog_command_error(self, ctx: commands.Context, error):
        await ctx.send(f"An error occurred in the Test cog: {error}")
