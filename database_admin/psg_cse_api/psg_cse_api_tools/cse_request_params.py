def create_calc_parameter():
    calc_parameters = {
        'Key': 'Parameters',
        'List': [
            {
                'Key': 'countingresults',
                'Value': 'true',
                'ValueType': 'boolean'
            },
            {
                'Key': 'ipaddress',
                'Value': {'type': 'string', '#text': '10.0.0.1'},
                'ValueType': 'string'
            }
        ]
    }
    return calc_parameters


def create_geography_parameter(city):
    geography_parameter = {
        'Key': 'parameters',
        'List': [{
            'Key': 'Reference',
            'Value': 'Geography',
            'ValueType': 'string'
        },
            {
                'Key': 'Search',
                'Value': f'{city} г',
                'ValueType': 'string'
            }]
    }
    return geography_parameter


def create_calc_data(city_sender, city_recipient, urgency, type_of_cargo, weight,
                     delivery_type, lenght, width, height, declared_value_rate):
    delivery_type_dict = {
        '': '',
        'Дверь-Дверь': 'ДоставкаДоДверей',
        'Склад-Дверь': 'СкладДверь',
        'Дверь-Склад (самовывоз)': 'Самовывоз',
        'Склад-Склад(самовывоз)': 'СкладСклад',
        'с возвратом': 'ДоставкаСВозвратом',
        'с уведомлением': 'ДоставкаСУведомлением',
        'с возвратом и уведомлением': 'ДоставкаСВозвратомУведомлением',
        'COD': 'ДоставкаCOD',
        'Почтовая комната': 'ПочтоваяКомната'
    }

    urgency_dict = {
        '': '',
        'Сборный груз': '4df477bc-a023-11eb-80dd-0090faaaf5c4',
        'Суточная': '9d7b9bdc-772f-11dc-a1ad-0015170f8c09',
        'Стандартная': '18c4f209-458b-11dc-9497-0015170f8c09',
        'Срочная': '18c4f207-458b-11dc-9497-0015170f8c09',
        'Сверхсрочная': '18c4f208-458b-11dc-9497-0015170f8c09',
        'Эконом-доставка': '8bbab642-1df3-11de-bcd5-0015170f8c09',
        'Срочная с тепловым режимом': '5d451adb-fa4d-11e0-a657-001e67086478'
    }

    type_of_cargo_dict = {
        '': '',
        'Документы': '81dd8a13-8235-494f-84fd-9c04c51d50ec',
        'Груз': '4aab1fc6-fc2b-473a-8728-58bcd4ff79ba',
        'Негабаритный груз': 'f132d9fa-a944-4c11-9001-f4dfdd13b4a7',
        'Опасный груз': 'dd80f922-a010-422a-b26a-0a65a6f894ce',
        'Сборный груз': 'c9d0c672-e908-11e9-bc2e-005056b646f7'
    }

    dimensions = {
        'Length': lenght,
        'Width': width,
        'Height': height
    }
    print((dimensions['Length']), (dimensions['Width']), (dimensions['Height']))
    volume = float(dimensions['Length']) * float(dimensions['Width']) * float(dimensions['Height'])
    volume_weight = volume / 5000

    calc_data = {
        'Key': 'Destinations',
        'List': {
            'Key': 'Destination',
            'Fields': [{'Key': 'SenderGeography', 'Value': f'{city_sender}', 'ValueType': 'string'},
                       {'Key': 'RecipientGeography', 'Value': f'{city_recipient}', 'ValueType': 'string'},
                       {'Key': 'Urgency', 'Value': f'{str(urgency_dict[str(urgency)])}', 'ValueType': 'string'},
                       {'Key': 'TypeOfCargo', 'Value': f'{str(type_of_cargo_dict[str(type_of_cargo)])}',
                        'ValueType': 'string'},
                       {'Key': 'Weight', 'Value': f'{weight}', 'ValueType': 'float'},
                       {'Key': 'Qty', 'Value': '1', 'ValueType': 'int'},
                       {'Key': 'DeliveryType', 'Value': f'{str(delivery_type_dict[str(delivery_type)])}',
                        'ValueType': 'string'},
                       {'Key': 'DeclaredValueRate', 'Value': f'{declared_value_rate}', 'ValueType': 'float'},
                       {'Key': 'Volume', 'Value': f'{volume}', 'ValueType': 'float'},
                       {'Key': 'VolumeWeight', 'Value': f'{volume_weight}', 'ValueType': 'float'},
                       {'Key': 'CountOnlyAddServices', 'Value': 'false', 'ValueType': 'boolean'}
                       ],
            'Tables': {'Key': 'AdditionalServices',
                       'List': {'Key': 'Объявленная стоимость',
                                'Value': '6da21fe7-4f13-11dc-bda1-0015170f8c09',
                                'ValueType': 'string'
                                },
                       },
        }
    }
    return calc_data
