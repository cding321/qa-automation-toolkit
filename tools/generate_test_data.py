from faker import Faker
from datetime import timedelta
import json
import argparse
import os

fake = Faker()


def generate_random_date():
    return fake.date_between(start_date='-1y', end_date='today')


def generate_booking(num_booking):
    bookings = []

    for _ in range(num_booking):
        check_in = generate_random_date()
        check_out = check_in + timedelta(days=fake.random_int(min=1, max=14))
        booking = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "total_price": fake.random_int(min=50, max=5000),
            "deposit_paid": fake.boolean(),
            "booking_dates": {
                "check_in": str(check_in),
                "check_out": str(check_out)
            },
            "additional_needs": fake.sentence(nb_words=3)
        }
        bookings.append(booking)
    return bookings


def save_bookings_to_json(bookings,output_dir):
    os.makedirs(output_dir, exist_ok=True)

    with open(f'{output_dir}/generated_bookings.json','w') as f:
        json.dump(bookings, f, indent=4)


def positive_int(value):
    value = int(value)

    if value <= 0:
        raise ValueError('Negative integers are not allowed')

    return value


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=positive_int, default=5)
    parser.add_argument('--output',default='data')

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_arguments()
    bookings = generate_booking(args.count)
    save_bookings_to_json(bookings,args.output)

