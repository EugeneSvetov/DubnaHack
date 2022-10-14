
from aiogram import types

from keyboards.inline.webappbutton import webapp_button
from loader import dp
from states.state import StateBot


@dp.message_handler(commands=['makeorder'], state=StateBot.is_client)
async def bot_start(message: types.Message):
    await message.answer(f'Вот ваш телеграмм id : <code>{str(message.from_user.id)}</code>, он вам пригодится при оформлении заказа\n\nПосле оформления заказа напишите команду "/buy", чтобы оплатить и получить ваш чек', reply_markup=webapp_button)
    await StateBot.client_is_paying.set()
