from dotenv import load_dotenv
import os
load_dotenv()

from SustainableBot import SustainBot

bot = SustainBot()

if __name__ == '__main__':
    bot.run(os.getenv("TOKEN"))