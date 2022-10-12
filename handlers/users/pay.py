# -*- coding: utf-8 -*-

import ast

from aiogram import types
from aiogram.types.message import ContentType
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.config import PAYMENTS_TOKEN
from loader import dp, bot
from states.state import StateBot


@dp.message_handler(commands=['buy'], state=StateBot.client_is_paying)
async def buy(message: types.Message):
    def get_order():
        owner_id = str(message.from_user.id)
        engine = create_engine(
            f'postgresql://etmlokgwbnykro:c41c54ac5c89c73e23a3ee26e827115b04acbdf6322a5cefad144bab37ae1aef@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d5n6nt2sh4lhdl')
        session = Session(bind=engine)
        id = session.execute(f'SELECT id FROM webapp_profile WHERE tg_id={owner_id}').fetchall()
        query = session.execute(
            f'SELECT * FROM webapp_order WHERE owner_id={id[0][0]} ORDER BY date_of_create DESC').first()
        session.close()
        dishes = ast.literal_eval(query[1])
        prices = ast.literal_eval(query[5])
        sales = query[13]
        if sales != 0:
            prices_with_sales = map(lambda x, y: x - y, prices, sales)
            order = dict(zip(prices_with_sales, dishes))
        else:
            order = dict(zip(prices, dishes))
        tg_prices = []
        for k, v in order.items():
            tg_prices.append(types.LabeledPrice(label=v, amount=int(k) * 100))
        return tg_prices

    def get_rest():
        owner_id = str(message.from_user.id)
        engine = create_engine(
            f'postgresql://etmlokgwbnykro:c41c54ac5c89c73e23a3ee26e827115b04acbdf6322a5cefad144bab37ae1aef@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d5n6nt2sh4lhdl')
        session = Session(bind=engine)
        id = session.execute(f'SELECT id FROM webapp_profile WHERE tg_id={owner_id}').fetchall()
        query = session.execute(
            f'SELECT * FROM webapp_order WHERE owner_id={id[0][0]} ORDER BY date_of_create DESC').fetchall()
        restaurant_id = (query[0][12])
        restaurants = session.execute(f'SELECT title FROM webapp_restaurant WHERE id={restaurant_id}').fetchall()
        session.close()
        restaurant = restaurants[0][0]
        return restaurant

    await bot.send_invoice(message.chat.id,
                           title=f"Заказ из ресторана {get_rest()}",
                           description=" ",
                           provider_token=PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://itadakimasuanime.files.wordpress.com/2014/11/tataki-salad-tempura-fate-stay-night-unlimited-blade-works-04.png",
                           photo_width=2880,
                           photo_height=1620,
                           photo_size=2880,
                           need_email=True,
                           need_phone_number=True,
                           need_shipping_address=False,
                           prices=get_order(),
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


@dp.pre_checkout_query_handler(lambda query: True, state=StateBot.client_is_paying)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT, state=StateBot.client_is_paying)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    await bot.send_message(message.chat.id,
                           f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно.\nЧтобы получить чек, нажмите выше на кнопку "Чек"')
    await StateBot.is_client.set()