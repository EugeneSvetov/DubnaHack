from aiogram import executor

from loader import dp
from utils.set_bot_commands import set_default_commands
import handlers


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)



if __name__ == '__main__':
    executor.start_polling(dp)
