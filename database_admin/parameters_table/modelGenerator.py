from django.contrib import admin
import psycopg2
from django.db.models.expressions import NoneType
from psycopg2 import Error
from django.db import models
from django.conf import settings


def get_data():
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
            database=settings.DATABASES['default']['NAME']
        )

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from table_002_parameters"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        return mobile_records
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def get_columns():
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
            database=settings.DATABASES['default']['NAME']
        )

        cursor = connection.cursor()

        postgre_sql_select_query = "SELECT column_name FROM information_schema.columns WHERE " \
                                   "table_name = \'table_002_parameters\';"

        cursor.execute(postgre_sql_select_query)
        mobile_records = cursor.fetchall()
        table_columns = []

        for row in mobile_records:
            table_columns.append(row[0])

        return table_columns

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


