from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
import time
from custom_collector_package.smoke_test import *


class RestfulCustomBookerCollector(object):
    # def __init__(self, c_base_url):
    #     self.base_url = c_base_url
    #     self.authentication_url = f"{c_base_url}/auth"
    #     self.get_bookings_url = f"{c_base_url}/bookings"

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
