#!/usr/bin/env python3
import sqlite3

class SQLiteDB:

    __slots__ = "__conexion", "__cursor"

    def __init__(self, database):
        self.set_database(database)

    def set_database(self, database):
        self.__conexion = sqlite3.connect(database)
        self.__cursor   = self.__conexion.cursor()

    def execute(self, query, commit=True):
        self.__cursor.execute(query)

        if query.upper().strip().startswith('SELECT'):
            data = self.__cursor.fetchall()
        else:
            if commit:
                self.commit()
            data = self.__conexion.total_changes
        return data

    def commit(self):
        self.__conexion.commit()

    def __del__(self):
        self.__cursor.close()
        self.__conexion.close()