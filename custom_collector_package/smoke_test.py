import requests


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
