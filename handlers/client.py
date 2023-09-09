import logging
import asyncio
import datetime
import sqldb
from peewee import *
from aiogram.types.web_app_info import WebAppInfo


from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from datetime import datetime as dt
from aiogram.utils.markdown import text, hbold
from aiogram.utils.exceptions import MessageNotModified
from contextlib import suppress
import keyboards as kb
from load_bot import bot, dp


async def command_start(message: types.Message, state: FSMContext):
    logging.info(f"{message.from_user.id} - start")
    user = sqldb.User.basic_auth(chat_id=message.from_user.id)

    if not isinstance(user, sqldb.User):
        user = sqldb.User.create_new(chat_id=message.from_user.id)

    msg_text = 'Run Bot with button'
    msg = await bot.send_message(chat_id=message.from_user.id, text=msg_text, reply_markup=kb.StartMenu())


def reg_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state="*")
    # dp.register_message_handler(echo_send)
    # dp.register_callback_query_handler(back_start, kb.FiltersMenu.CallbackData.FILTER_CB.filter(ACTION=["BACK"]))

