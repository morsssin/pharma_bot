# -*- coding: utf-8 -*-
import os
import config
import logging
import datetime

from aiogram.utils import executor

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2


storage = RedisStorage2(config.REDIS_HOST, config.REDIS_PORT)
bot = Bot(config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
