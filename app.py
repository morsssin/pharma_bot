# -*- coding: utf-8 -*-
import os
import logging
import asyncio
import datetime

from aiogram.utils import executor
import sqldb
from load_bot import bot, dp



async def on_startup(dp):
    sqldb.create_tables()
    logging.info('Bot loaded')


async def on_shutdown(dp):
    logging.info('Shutting down..')
    sqldb.close_conn()
    await dp.storage.close()
    logging.info("DB Connection closed")


if __name__ == "__main__":
    from handlers import client

    logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    filename = os.path.join(logs_dir, datetime.date.today().strftime("%d_%m_%Y") + "_log.log")
    # logging.basicConfig(level=logging.INFO, filename=filename, filemode="a",
    #                     format='[%(asctime)s] %(filename)s [LINE:%(lineno)d] #%(levelname)-8s %(message)s')
    logging.basicConfig(level=logging.INFO,
                        # filename=filename, filemode="a",
                        format='[%(asctime)s] %(filename)s [LINE:%(lineno)d] #%(levelname)-8s %(message)s')

    client.reg_handlers_client(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
