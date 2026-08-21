import json
import os

import pytest
import subprocess

from tools.generate_test_data import generate_booking
from datetime import date


def test_generate_booking_count():
    num_booking = 5
    bookings = generate_booking(num_booking)
    assert len(bookings) == num_booking, f"Expected {num_booking} bookings, but got {len(bookings)}"


def test_data_comparison():
    bookings = generate_booking(5)
    for booking in bookings:
        checkin = date.fromisoformat(booking["booking_dates"]["check_in"])
        checkout = date.fromisoformat(booking["booking_dates"]["check_out"])
        assert checkout > checkin


def test_data_types():
    bookings = generate_booking(5)
    for booking in bookings:
        assert isinstance(booking["first_name"], str)
        assert isinstance(booking["last_name"], str)
        assert isinstance(booking["total_price"], int)
        assert isinstance(booking["deposit_paid"], bool)
        assert isinstance(booking["booking_dates"]["check_in"], str)
        assert isinstance(booking["booking_dates"]["check_out"], str)
        assert isinstance(booking["additional_needs"], str)


def test_price_range():
    bookings = generate_booking(5)
    for booking in bookings:
        assert 50 <= booking["total_price"] <= 5000


def test_booking_structure():
    bookings = generate_booking(5)

    expected_keys = {"first_name", "last_name", "total_price", "deposit_paid", "booking_dates", "additional_needs"}

    for booking in bookings:
        assert set(booking.keys()) == expected_keys


def test_date_duration():
    bookings = generate_booking(5)
    for booking in bookings:
        checkin = date.fromisoformat(booking["booking_dates"]["check_in"])
        checkout = date.fromisoformat(booking["booking_dates"]["check_out"])
        assert 1 <= (checkout - checkin).days <= 14


@pytest.fixture
def generated_bookings(tmp_path):
    def _generate(count=None):
        if count is not None:
            result = subprocess.run(["python","tools/generate_test_data.py", "--count", str(count), "--output", str(tmp_path)])
        else:
            result = subprocess.run(["python","tools/generate_test_data.py", "--output", str(tmp_path)])

        assert result.returncode == 0

        output_file = tmp_path / "generated_bookings.json"

        with open(output_file) as f:
            bookings = json.load(f)
        return bookings
    return _generate


def test_cli_count(generated_bookings):
    #result = subprocess.run(["python","tools/generate_test_data.py", "--count", "10"])
    #assert result.returncode == 0
    # with open("data/generated_bookings.json") as f:
    #     bookings = json.load(f)
    # assert len(bookings) == 10
    bookings = generated_bookings(10)
    assert len(bookings) == 10


def test_cli_default_count(generated_bookings):
    #result = subprocess.run(["python","tools/generate_test_data.py"])
    #assert result.returncode == 0
    #with open("data/generated_bookings.json") as f:
    #    bookings = json.load(f)
    #assert len(bookings) == 5

    bookings = generated_bookings()
    assert len(bookings) == 5


def test_cli_invalid_count():
    result = subprocess.run(["python","tools/generate_test_data.py", "--count", "abc"])
    assert result.returncode != 0


def test_cli_negative_count():
    result = subprocess.run(["python","tools/generate_test_data.py", "--count", "-5"])
    assert result.returncode != 0


def test_cli_existing_output_dir(tmp_path):
    output_dir = tmp_path / "test_data"
    output_dir.mkdir()

    assert output_dir.exists()

    result = subprocess.run(["python","tools/generate_test_data.py", "--output", str(output_dir)])
    assert result.returncode == 0
    assert (output_dir / "generated_bookings.json").exists()


def test_cli_new_output_dir(tmp_path):
    output_dir = tmp_path / "test_data_new"

    assert not output_dir.exists()

    result = subprocess.run(["python", "tools/generate_test_data.py", "--output", str(output_dir)])
    assert result.returncode == 0
    assert output_dir.exists()
    assert (output_dir / "generated_bookings.json").exists()

