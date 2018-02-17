# -*- coding: utf-8 -*-
"""
    DB Helpers
    ----------

    Module contains shared functionality for working with PostgreSQL database

"""

import os
from contextlib import contextmanager

import psycopg2
from psycopg2.extras import DictCursor

#: Connection parameters to establish connection to PostgreSQL database
DB_PARAMS = {"dbname": os.environ.get("DB_NAME"),
             "user": os.environ.get("DB_USERNAME"),
             "password": os.environ.get("DB_PASSWORD"),
             "host": os.environ.get("DB_HOST"),
             "port": os.environ.get("DB_PORT")}


@contextmanager
def yield_db_cursor(connect_params=DB_PARAMS, cursor_type=DictCursor):
    """Returns database cursor to interact with PostgreSQL database.

    :param connect_params: database connection parameters
    :type connect_params: dict
    :param cursor_type: specify the type of cursor to return (tuple, dict)
    :type cursor_type: obj
    :returns: context based PostgreSQL  database cursor
    :rtype: psycopg2.cursor
    """

    with psycopg2.connect(**connect_params) as con:
        with con.cursor(cursor_factory=cursor_type) as cur:
            yield cur
