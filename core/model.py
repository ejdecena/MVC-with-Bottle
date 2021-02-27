#!/usr/bin/env python3
import os
import abc
import json
from core.exceptions.modelexception import ModelException
from core.libs.sqlitedb import SQLiteDB


class Model(SQLiteDB, metaclass=abc.ABCMeta):

    def __init__(self):
        with open("config.json".format(os.sep)) as fconfig:
            config = json.load(fconfig)
            super().__init__("data{}{}".format(os.sep, config["database"]))