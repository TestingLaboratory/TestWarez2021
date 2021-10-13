import requests
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY

__headers = {
    'Content-Type': 'application/json'
}


def check_login():
    authentication_url = 'https://restful-booker.herokuapp.com/auth'
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(authentication_url,
                             headers=__headers,
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
        token_retrieved = 1 if access_token else 0
        metric_was_login_successful = GaugeMetricFamily('access_token_retrieved',
                                                        'Retrieval of access token',
                                                        value=token_retrieved)
        yield metric_was_login_successful
        bookings = check_bookings()
        bookings_retrieved = 1 if bookings else 0
        metric_are_there_any_bookings = GaugeMetricFamily('booking_id_retrieved',
                                                          'Retrieval of existing bookings',
                                                          value=bookings_retrieved)
        yield metric_are_there_any_bookings


if __name__ == "__main__":
    REGISTRY.register(RestfulCustomBookerCollector())
    start_http_server(9099)
    # while True:
    #     time.sleep(1)
