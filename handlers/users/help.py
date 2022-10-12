# -*- coding: utf-8 -*-

from aiogram import types

from loader import dp
from states.state import StateBot


@dp.message_handler(commands=['help'], state=StateBot.is_client)
async def bot_start(message: types.Message):
    await message.answer(
        "❗️Справка по текущим командам:\n\n▪️/makeorder ➖ оформить заказ\n\n▪️ /help ➖ вывести список актуальных команд\n▪️ /start ➖ запустить бота\n▪️ /login ➖ войти как сотрудник ресторана\n▪️ /ref — получить свою ссылку для приглашения\n▪️ /buy - оплатить и получить чек оплаты")
