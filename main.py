import logging

from aiogram import Bot, Dispatcher, executor, types
from environs import Env

from wikitest import send_eiki

env = Env()
env.read_envfile('.env')
API_TOKEN = env.str("API_TOKEN")


# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):

    text = "maqola topish uchun ao'z yuboring"

    await message.reply(text)



@dp.message_handler()
async def echo(message: types.Message):
    try:
        result = send_eiki(message.text)  # bu oddiy function
        await message.reply(result)
    except Exception:
        await message.reply("Bunday maqola topilmadi!")


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)