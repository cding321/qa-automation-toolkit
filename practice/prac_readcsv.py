import csv
import sys

def solution():
    #with open("practice/input_test_readcsv.csv") as f:
    #    reader = csv.DictReader(f)
    reader = csv.DictReader(sys.stdin)

    result = {}
    for row in reader:
        if row["status"] == "COMPLETED":
            user_id = row["user_id"]
            amt = float(row["amount"])

            result[user_id] = result.get(user_id, 0) + amt

            '''
            if user_id in result:
                result[user_id] = result[user_id] + amt
            else:
                result[user_id] = amt
            '''

    for id, record in sorted(result.items()):
        if record >= 100:
            print(id, record)


def solution_email():
    reader = csv.DictReader(sys.stdin)
    result = {}

    for row in reader:
        email = row["email"]

        if email not in result:
            result[email] = row
        else:
            if row["updated_at"] > result[email]["updated_at"]:
                result[email] = row

    for email, row in sorted(result.items()):
        if row["status"] == "ACTIVE":
            print(email, row["customer_id"])




