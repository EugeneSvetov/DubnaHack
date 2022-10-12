# -*- coding: utf-8 -*-

import ast

from aiogram import types
from aiogram.types.message import ContentType
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.config import PAYMENTS_TOKEN
from loader import dp, bot
from states.state import StateBot


@dp.message_handler(commands=['buy'], state=StateBot.is_client)
async def buy(message: types.Message):
    def get_order():
        owner_id = str(message.from_user.id)
        engine = create_engine(
            f'postgresql://etmlokgwbnykro:c41c54ac5c89c73e23a3ee26e827115b04acbdf6322a5cefad144bab37ae1aef@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d5n6nt2sh4lhdl')
        session = Session(bind=engine)
        id = session.execute(f'SELECT id FROM webapp_profile WHERE tg_id={owner_id}').fetchall()
        query = session.execute(
            f'SELECT * FROM webapp_order WHERE owner_id={id[0][0]} ORDER BY date_of_create DESC').fetchall()
        session.close()
        dishes = ast.literal_eval(query[0][1])
        prices = ast.literal_eval(query[0][5])
        counts = ast.literal_eval(query[0][2])
        sales = query[0][13]
        print(sales)
        new_prices = map(lambda x, y: x * y, prices, counts)
        print(new_prices)
        if sales != 0:
            prices_with_sales = map(lambda x, y: x - y, new_prices, sales)
            order = dict(zip(prices_with_sales, dishes))
        else:
            order = dict(zip(new_prices, dishes))
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
        restaurant = restaurants[0][0]
        return restaurant

    await bot.send_invoice(message.chat.id,
                           title="Ваш заказ готов к оплате",
                           description=f"Заказ из ресторана {get_rest()}",
                           provider_token=PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://www.clipartkey.com/mpngs/m/327-3271974_burger-font.png",
                           photo_width=900,
                           photo_height=560,
                           photo_size=900,
                           need_email=True,
                           need_phone_number=True,
                           need_shipping_address=False,
                           prices=get_order(),
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")
    await StateBot.is_client.finish()