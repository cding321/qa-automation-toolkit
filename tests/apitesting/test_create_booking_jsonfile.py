import json

from playwright.sync_api import Playwright


def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"

    request_context = playwright.request.new_context()

    file = open("data/post_request_body.json","r")
    request_body= json.load(file)

    response = request_context.post(f"{base_url}/booking",data=request_body)

    assert response.ok
    assert response.status == 200

    response_body = response.json()
    print("Response body =====>",response_body)

    assert "bookingid" in response_body
    assert "booking" in response_body

    booking = response_body["booking"]
    assert booking["firstname"] == "Jim"
    assert booking["lastname"] == "Brown"
    assert booking["totalprice"] == 1000
    assert booking["depositpaid"] is True
    assert booking["bookingdates"]["checkin"] == "2025-07-01"
    assert booking["bookingdates"]["checkout"] == "2025-07-05"
    assert booking["additionalneeds"] == "super bowls"

    request_context.dispose()

