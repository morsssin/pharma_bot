# -*- coding: utf-8 -*-
import os
import logging
import sqlite3 as sq

from peewee import *
from datetime import datetime

db = SqliteDatabase(r'bot_db.db', pragmas={'journal_mode': 'wal', 'foreign_keys': "on",'wal_autocheckpoint': 10})


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    chat_id = BigAutoField(primary_key=True)
    user_type = CharField(default='user')

    @staticmethod
    def basic_auth(chat_id):
        return User.get_or_none(chat_id=chat_id)

    @staticmethod
    def create_new(chat_id):
        new_user = User.create(chat_id=chat_id)
        new_user.save()
        return User.get_or_none(chat_id=chat_id)


class UserSettings(BaseModel): # TO DO create settings profile for every user
    chat_id = BigAutoField(primary_key=True)


class RequestTable(BaseModel):
    id = AutoField(primary_key=True)
    user_id = BigIntegerField()
    request_id = CharField()
    status = CharField()


def create_tables():
    # db.connect()
    db.create_tables([User, UserSettings, RequestTable])
    # Tasks.base_init()


def close_conn():
    db.close()

