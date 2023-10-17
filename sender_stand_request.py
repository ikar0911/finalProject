import configuration
import requests
import data
import datetime


def post_new_order():  # Функция создания нового заказа
    order_body = data.headers_order
    order_data = datetime.date.today() + datetime.timedelta(days=1)
    str_order_data = f"{order_data}"
    order_body["deliveryDate"] = str_order_data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)


def get_order(track_id):  # Функция получения заказа по его номеру
    param_t = {'t': track_id}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=param_t,
                        headers=data.headers)
