import typing
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.web_app_info import WebAppInfo


class StartMenu(InlineKeyboardMarkup):
    def __init__(self):
        super().__init__(row_width=2)
        self.b1 = InlineKeyboardButton('Run Bot', web_app=WebAppInfo(url='https://itproger.com/'))
        # self.b2 = InlineKeyboardButton('Name 2', callback_data=self.CallbackData.START_CB.new(ACTION="2"))

        self.add(self.b1)

    class CallbackData:
        START_CB = CallbackData("START", "ACTION")

cancel_kb = InlineKeyboardMarkup()
cancel_button = InlineKeyboardButton('❌ Отмена', callback_data='cancel_call_b')
cancel_kb.add(cancel_button)
