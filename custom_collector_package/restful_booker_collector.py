from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
import time
import requests


# from custom_collector_package.smoke_test import *

def check_login():
    authentication_url = 'https://restful-booker.herokuapp.com/auth'
    payload = "{\n    \"username\" : \"admin\",\n    \"password\" : \"password123\"\n}"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(authentication_url, headers=headers,
                             data=payload)
    json_res = response.json()
    access_token = json_res['token']
    return access_token


def check_bookings():
    bookings_url = 'https://restful-booker.herokuapp.com/bookings'
    booking_response = requests.get(bookings_url, headers={'Content-Type': 'application/json'})
    bookings = booking_response.status_code
    return bookings


class RestfulCustomBookerCollector(object):
    def collect(self):
        access_token = check_login()
        is_token_retrieved = 0
        if access_token is None:
            is_token_retrieved = 0
        else:
            is_token_retrieved = 1

        metric_was_login_successful = GaugeMetricFamily('access_token_retrieved', 'Retrieval of access token',
                                                        value=is_token_retrieved)
        yield metric_was_login_successful
        bookings = check_bookings()
        are_bookings_retrieved = 0
        if bookings is None:
            are_bookings_retrieved = 0
        else:
            are_bookings_retrieved = 1

        metric_are_there_any_bookings = GaugeMetricFamily('booking_id_retrieved', 'Retrieval of existing bookings',
                                                          value=are_bookings_retrieved)
        yield metric_are_there_any_bookings


if __name__ == "__main__":
    REGISTRY.register(RestfulCustomBookerCollector())
    start_http_server(9099)
    while True:
        time.sleep(1)
