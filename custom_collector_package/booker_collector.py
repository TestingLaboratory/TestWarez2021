import time

import requests
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY
from prometheus_client.metrics_core import GaugeMetricFamily


class RestfulCustomBookerCollector:
    __headers = {'Content-Type': 'application/json'}

    def check_login(self):
        authentication_url = 'https://restful-booker.herokuapp.com/auth'

        payload = {
            "username": "admin",
            "password": "password123"
        }

        response = requests.post(authentication_url,
                                 headers=self.__headers,
                                 json=payload)

        access_token = response.json()['token']
        return access_token

    def check_bookings(self):
        bookings_url = 'https://restful-booker.herokuapp.com/bookings'
        booking_response = requests.get(bookings_url, headers=self.__headers)
        return booking_response.status_code

    def collect(self):
        access_token = self.check_login()
        token_retrieved = 1 if access_token else 0

        metric_was_login_successful = GaugeMetricFamily('access_token_retrieved',
                                                        'Retrieval of access token',
                                                        value=token_retrieved)
        yield metric_was_login_successful

        bookings = self.check_bookings()
        bookings_retrieved = 1 if bookings else 0

        metric_are_there_any_bookings = GaugeMetricFamily('booking_id_retrieved',
                                                          'Retrieval of existing bookings',
                                                          value=bookings_retrieved)
        yield metric_are_there_any_bookings


if __name__ == "__main__":
    REGISTRY.register(RestfulCustomBookerCollector())
    start_http_server(9099)
    while True:
        time.sleep(15)
