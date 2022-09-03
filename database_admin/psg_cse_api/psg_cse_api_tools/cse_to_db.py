import json
from datetime import datetime

from . import calc_func
from .db_queries_source import *
from .connection_to_database import create_connection


conn = ''


def insert_to_db(city_sender, city_recipient, urgency, type_of_cargo, weight,
                 delivery_type, lenght, width, height, declared_value_rate, is_test, sending_user):
    request_time = datetime.now()
    '''
    Генерация и отправка запроса Calc в API CSE.
    '''
    calc_func.create_request_cse(city_sender=city_sender,
                                 city_recipient=city_recipient,
                                 urgency=urgency,
                                 type_of_cargo=type_of_cargo,
                                 weight=weight,
                                 lenght=lenght,
                                 width=width,
                                 height=height,
                                 delivery_type=delivery_type,
                                 declared_value_rate=declared_value_rate,
                                 is_test=is_test
                                 )

    '''
    Если включена тестовая версия, результат а таблицу 'HTTP-запросы' не записывается.
    '''
    if is_test is True:
        return

    response_waiting_time = str((datetime.now() - request_time).total_seconds())
    connection = create_connection()
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(select_id)
        id_api = cursor.fetchall()

    if id_api == []:
        id_bd = 1
    else:
        id_bd = id_api[-1][-1]+1

    with connection.cursor() as cursor:
        if id_bd > 1:
            cursor.execute(select_request, (id_bd - 1, ))
            select_last_data = cursor.fetchone()
            print("Data select successfully")

    with connection.cursor() as cursor:
        if id_bd == 1:
            cursor.execute(insert_request,
                           (1,
                            json.dumps(calc_func.xml_data, ensure_ascii=False, indent=2),
                            calc_func.ready_response_calc,
                            request_time,
                            response_waiting_time,
                            int(sending_user)))
            print("Insert is successfully")
        elif id_bd > 1:
            cursor.execute(insert_request,
                           (id_bd,
                            json.dumps(calc_func.xml_data, ensure_ascii=False, indent=2),
                            calc_func.ready_response_calc,
                            request_time,
                            response_waiting_time,
                            int(sending_user)))
            print("Insert is successfully")

            cursor.execute(select_response, (id_bd,))
            select_next_data = cursor.fetchone()
            if select_next_data == select_last_data:
                print('No changes')


def send_calc_request(sending_user, city_sender, city_recipient, urgency, type_of_cargo, weight,
                      delivery_type, lenght, width, height, declared_value_rate, is_test):
    _urgency = str(urgency)
    _delivery_type = str(delivery_type)
    _type_of_cargo = str(type_of_cargo)
    if urgency is None:
        _urgency = ''
    if delivery_type is None:
        _delivery_type = ''
    if type_of_cargo is None:
        _type_of_cargo = ''
    if declared_value_rate is None:
        declared_value_rate = 0
    try:
        insert_to_db(sending_user=sending_user,
                     city_sender=city_sender,
                     city_recipient=city_recipient,
                     urgency=_urgency,
                     type_of_cargo=_type_of_cargo,
                     weight=weight,
                     lenght=lenght,
                     width=width,
                     height=height,
                     delivery_type=_delivery_type,
                     declared_value_rate=declared_value_rate,
                     is_test=is_test
                     )
    except Exception as _ex:
        print("[INFO]Error", _ex)
    finally:
        if conn:
            conn.close()
            print("[INFO]PostgreSQL connection close.")
