import sendor_stand_request
import requests
import data
import configuration


def test_get_order_track_code_200():
    assert sendor_stand_request.get_order_status_code_200() == 200