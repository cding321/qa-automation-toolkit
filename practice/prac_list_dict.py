def get_expensive_booking_ids(bookings):

    result = []

    for booking in bookings:
        if booking["totalprice"] > 200:
            result.append(booking["bookingid"])

    # result = [booking["bookingid"] for booking in bookings if booking["totalprice"] > 200]

    return result

print(get_expensive_booking_ids([
        {"bookingid": 101, "firstname": "Jim", "totalprice": 120},
        {"bookingid": 102, "firstname": "Alice", "totalprice": 250},
        {"bookingid": 103, "firstname": "Tom", "totalprice": 80},
        {"bookingid": 104, "firstname": "Lisa", "totalprice": 300},
    ])
)


def get_failed_endpoints(responses):

    result = []

    for response in responses:
        if response["status"] >= 400:
            result.append(response["endpoint"])

    return result

print(get_failed_endpoints([
        {"status": 200, "endpoint": "/users"},
        {"status": 404, "endpoint": "/users/123"},
        {"status": 200, "endpoint": "/booking"},
        {"status": 500, "endpoint": "/payment"},
        {"status": 200, "endpoint": "/login"},
    ])
)

def count_response_status(responses):

    success = 0
    failed = 0

    for response in responses:
        if 200 <= response["status"] < 300:
            success += 1
        elif response["status"] >= 400:
            failed += 1

    return success, failed

print(count_response_status([
        {"status": 200, "endpoint": "/users"},
        {"status": 404, "endpoint": "/users/123"},
        {"status": 200, "endpoint": "/booking"},
        {"status": 500, "endpoint": "/payment"},
        {"status": 200, "endpoint": "/login"},
    ])
)


def get_total_price(bookings):

    total_price = 0

    for booking in bookings:
        total_price += booking["totalprice"]

    return total_price


def get_checkin_date(booking):

    return booking["bookingdates"]["checkin"]


def count_status_codes(responses):

    status_count = {}

    for response in responses:
        status = response["status"]
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1

    return status_count


def get_endpoints_by_status(responses, target_status):

    result = []

    for response in responses:
        if response["status"] == target_status:
            result.append(response["endpoint"])

    return result


def find_missing_extra_ids(expected_ids, actual_ids):

    # missing_ids = []
    # extra_ids = []
    #
    # for id in expected_ids:
    #     if id not in actual_ids:
    #         missing_ids.append(id)
    #
    # for id in actual_ids:
    #     if id not in expected_ids:
    #         extra_ids.append(id)

    expected_set = set(expected_ids)
    actual_set = set(actual_ids)
    missing_ids = list(expected_set - actual_set)
    extra_ids = list(actual_set - expected_set)

    return missing_ids, extra_ids


def get_unpaid_bookings(bookings):

    unpaid_bookings = []

    for booking in bookings:
        if not booking["depositpaid"]:
            unpaid_bookings.append(booking["bookingid"])

    return unpaid_bookings

