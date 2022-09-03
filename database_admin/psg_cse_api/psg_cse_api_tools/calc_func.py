from zeep import Client
import json
from zeep import helpers

from .cse_request_params import create_calc_parameter, create_geography_parameter, create_calc_data


login = ''
password = ''
client = ''

city_sender_geography = ''
city_recipient_geography = ''
ready_response_calc = ''
ready_answer_calc_dict = ''
ready_answer_calc = {}
xml_data = {}


def create_request_cse(city_sender, city_recipient, urgency, type_of_cargo, weight,
                       delivery_type, lenght, width, height, declared_value_rate, is_test):
    global xml_data
    global ready_answer_calc
    global ready_response_calc
    global ready_answer_calc_dict
    global login
    global password
    global client

    if is_test is False:
        login = 'ПСГ (Казань)'
        password = 'FxzMF2XtSZBSPtd'
        client = Client('http://web.cse.ru/1c/ws/Web1C.1cws?wsdl')
    else:
        login = 'test'
        password = '2016'
        client = Client('http://lk-test.cse.ru/1c/ws/web1c.1cws?wsdl')

    xml_params_geography_sending = create_geography_parameter(city=city_sender)
    city_sender = client.service.GetReferenceData(login=login,
                                                  password=password,
                                                  parameters=xml_params_geography_sending)['List'][0]['Key']

    xml_params_geography_arrival = create_geography_parameter(city=city_recipient)
    city_recipient = client.service.GetReferenceData(login=login,
                                                     password=password,
                                                     parameters=xml_params_geography_arrival)['List'][0]['Key']

    xml_data = create_calc_data(city_sender=city_sender,
                                city_recipient=city_recipient,
                                urgency=urgency,
                                type_of_cargo=type_of_cargo,
                                weight=weight,
                                lenght=lenght,
                                width=width,
                                height=height,
                                delivery_type=delivery_type,
                                declared_value_rate=declared_value_rate
                                )
    ready_answer_calc = client.service.Calc(login=login,
                                            password=password,
                                            data=xml_data,
                                            parameters=create_calc_parameter()
                                            )
    ready_answer_calc_dict = helpers.serialize_object(ready_answer_calc, dict)
    ready_response_calc = json.dumps(ready_answer_calc_dict, default=str, ensure_ascii=False, indent=2)



