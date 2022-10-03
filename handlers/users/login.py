# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import message

from keyboards.inline.rest_list import rest_button

from loader import dp
from states.state import StateBot


@dp.message_handler(commands=['login'],state = StateBot.is_client)
async def bot_start(message: types.Message):
    await message.answer("👨‍🍳 Вы сотрудник ресторана? Выберете ресторан, на заказы из которого хотите получать уведомления",reply_markup=rest_button)

@dp.callback_query_handler(state = StateBot.is_client)
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    await call.answer(f'Вы успешно вошли как сотрудник {call.data}', show_alert=True)
    await state.update_data(
        {"Никнейм":call.from_user.full_name,
         "tg_id": call.from_user.id,
         "Заведение": call.data}
    )
    data = await state.get_data()
    print(f"{data['Никнейм']} : {data['tg_id']} : {data['Заведение']}")
    await StateBot.is_employee.set()


