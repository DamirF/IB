
def transform_respone(calc_dict):
    for item in calc_dict.copy():
        if not calc_dict[item]:
            calc_dict.pop(item)
        elif type(calc_dict[item]) == list:
            for i in calc_dict[item]:
                for item_list in i.copy():
                    if not i[item_list]:
                        i.pop(item_list)
                    elif type(i[item_list]) == list:
                        for j in i[item_list]:
                            for item_field in j.copy():
                                if not j[item_field]:
                                    j.pop(item_field)
                                elif type(j[item_field]) == list:
                                    for k in j[item_field]:
                                        for item_field_list in k.copy():
                                            if not k[item_field_list]:
                                                k.pop(item_field_list)
    return calc_dict
