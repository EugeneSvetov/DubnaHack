# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import message

from keyboards.inline.rest_list import rest_button
from keyboards.inline.login import  login_button

from loader import dp
from states.state import StateBot


@dp.message_handler(commands=['login'],state = StateBot.is_client)
async def bot_start(message: types.Message):
    await message.answer("👨‍🍳 Вы сотрудник ресторана? Выберете ресторан, на заказы из которого хотите получать уведомления",reply_markup=rest_button)

@dp.callback_query_handler(state = StateBot.is_client)
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    await call.answer(f'Вы успешно вошли как сотрудник', True)
    print(f'{call.from_user.full_name} : {call.from_user.id}')
    await state.update_data(
        {"tg_id": call.from_user.id}
    )
    await call.message.answer('<strong>Отлично</strong>\n'
                              'Теперь вы сотрудник')
    await StateBot.is_employee.set()
