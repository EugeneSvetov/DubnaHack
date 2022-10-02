from aiogram import executor
from aiogram.dispatcher import FSMContext

from utils.set_bot_commands import set_default_commands
import handlers
from aiogram import types
from keyboards.inline.webappbutton import *
from loader import dp

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)



if __name__ == '__main__':
    executor.start_polling(dp)
