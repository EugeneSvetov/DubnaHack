# -- coding: utf-8 --
from aiogram.dispatcher.filters.state import StatesGroup, State



class StateBot(StatesGroup):
    is_employee = State()
    is_client = State()
    client_is_paying = State()