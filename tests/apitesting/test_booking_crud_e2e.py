import json

import pytest
from playwright.sync_api import Playwright
from tools.generate_test_data import generate_booking

base_url = "https://restful-booker.herokuapp.com"

def read_json(file_path):
    file = open(file_path, "r")
    return json.load(file)

# fixture
@pytest.fixture(scope="session")
def request_context(playwright: Playwright):
    context = playwright.request.new_context()
    yield context
    context.dispose()


@pytest.fixture
def generated_bookings(request):
    count = request.config.getoption("--booking-count")
    return generate_booking(count)


def test_create_booking(request_context):
    data = read_json("data/post_request_body.json")
    response = request_context.post(f"{base_url}/booking", data=data)
    assert response.ok, "POST request failed"
    assert response.status == 200

    response_body=response.json()
    print("Create Booking Response", response_body)

    assert "bookingid" in response_body
    assert "booking" in response_body

    booking = response_body["booking"]

    assert booking["firstname"] == data["firstname"]
    assert booking["lastname"] == data["lastname"]
    assert booking["totalprice"] == data["totalprice"]
    assert booking["depositpaid"] == data["depositpaid"]
    assert booking["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]

    global booking_id
    booking_id = response_body["bookingid"]


def test_get_booking_by_id(request_context):
    response = request_context.get(f"{base_url}/booking/{booking_id}")
    assert response.ok
    assert response.status == 200

    response_body=response.json()
    print("Booking details fetched by ID", response_body)
    assert "firstname" in response_body
    assert "lastname" in response_body


def test_get_booking_by_name(request_context):

    names_params = {"firstname":"Jim", "lastname":"Brown"}

    response = request_context.get(f"{base_url}/booking", params=names_params)

    assert response.ok
    assert response.status == 200

    response_body=response.json()

    print(f"Booking IDs fetched by Names {names_params}", response_body)

    assert len(response_body) > 0

    for item in response_body:
        assert "bookingid" in item


def test_get_booking_by_dates(request_context):
    dates_params = {"checkin": "2025-12-15", "checkout": "2025-12-20"}

    response = request_context.get(f"{base_url}/booking", params=dates_params)

    assert response.ok
    assert response.status == 200

    response_body = response.json()

    print(f"Booking IDs fetched by Dates {dates_params}", response_body)

    for item in response_body:
        assert "bookingid" in item


def test_create_token(request_context):
    data = read_json("data/token_request_body.json")
    response = request_context.post(f"{base_url}/auth", data=data)
    assert response.ok
    assert response.status == 200

    response_body=response.json()
    print("Token Creation Response", response_body)

    assert "token" in response_body

    global token
    token = response_body["token"]

    assert len(token) > 5


def test_partial_update_booking(request_context):
    data = read_json("data/patch_request_body.json")
    response = request_context.patch(f"{base_url}/booking/{booking_id}",
                                     data=data,
                                     headers={"Cookie": f"token={token}"})
    assert response.ok
    assert response.status == 200

    response_body=response.json()
    print(f"Partial Update Response for bookding id {booking_id}", response_body)

    for key in data.keys():
        assert key in response_body
        assert response_body[key] == data[key]


def test_full_update_booking(request_context):
    data = read_json("data/put_request_body.json")
    response = request_context.patch(f"{base_url}/booking/{booking_id}",
                                     data=data,
                                     headers={"Cookie": f"token={token}"})
    assert response.ok
    assert response.status == 200

    response_body = response.json()
    print(f"Full Update Response for booking id {booking_id}", response_body)

    for key in data.keys():
        assert key in response_body
        assert response_body[key] == data[key]

    assert response_body["firstname"] == data["firstname"]
    assert response_body["lastname"] == data["lastname"]
    assert response_body["totalprice"] == data["totalprice"]


def test_delete_booking(request_context):
    response = request_context.delete(f"{base_url}/booking/{booking_id}",
                           headers={"Cookie": f"token={token}"})

    assert response.status == 201
    print("Booking successfully deleted ----> ID", booking_id)


def test_create_booking_with_generated_data(request_context,generated_bookings):
    # data = read_json("data/generated_bookings.json")
    print(f"Generated bookings:{len(generated_bookings)}")

    for booking_data in generated_bookings:
        print("sending booking:",booking_data)
        response = request_context.post(f"{base_url}/booking", data=booking_data)

        assert response.ok, "POST request failed"
        assert response.status == 200

        response_body = response.json()

        assert "bookingid" in response_body
        assert "booking" in response_body

        booking = response_body["booking"]

        assert booking["firstname"] == booking_data["firstname"]
        assert booking["lastname"] == booking_data["lastname"]
        assert booking["totalprice"] == booking_data["totalprice"]
        assert booking["depositpaid"] == booking_data["depositpaid"]
        assert booking["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
        assert booking["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
        assert booking["additionalneeds"] == booking_data["additionalneeds"]

