from dotenv import load_dotenv
import os
load_dotenv()

from SustainableBot import SustainBot
from SustainableBot import My_World
from SustainableBot import Info

bot = SustainBot()

if __name__ == '__main__':
    bot.add_cog(My_World(bot))
    bot.add_cog(Info(bot))
    bot.run(os.getenv("TOKEN"))