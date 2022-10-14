# -*- coding: utf-8 -*-
import ast

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from loader import *
from states.state import StateBot


@dp.message_handler(commands=['log_out'], state=StateBot.is_employee)
async def bot_exit(call: types.CallbackQuery):
    await call.answer("Вы успешно вышли из состояния сотрудника")
    await StateBot.is_client.set()