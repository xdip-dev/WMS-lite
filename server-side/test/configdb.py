import psycopg2
import os
from dotenv import load_dotenv, find_dotenv
import pytest

import repackage
repackage.up()
import helper
from db.tableInfo import Tableinformation

load_dotenv(find_dotenv(helper.pathGeneratorMainToFile(["server-side", ".env"])))


@pytest.fixture(scope='module')
def cnxn():
    password = os.getenv("password")
    connectionString = f"dbname=wms user=postgres password={password}"
    connection =psycopg2.connect(connectionString)
    yield connection
    connection.close()

@pytest.fixture
def cursor(connection):
    cursor = connection.cursor()
    yield cursor
    connection.rollback()

