# Козубенко Иван, 18 когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER + '?t=' + str(track),
                        headers=data.headers)


def get_order_status_code_200():
    response_code = post_new_order(data.order_body)
    track = response_code.json()["track"]
    return get_order_track(track).status_code


def test_get_order_track_code_200():
    assert get_order_status_code_200() == 200
