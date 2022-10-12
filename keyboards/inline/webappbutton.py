from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

inline_button_1 = InlineKeyboardButton('🍽 Оформить заказ',
                                       web_app=WebAppInfo(url='https://tg-webappl.herokuapp.com/'))
webapp_button = InlineKeyboardMarkup().add(inline_button_1)
