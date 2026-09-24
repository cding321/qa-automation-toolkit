'''
import json
import sys
for line in sys.stdin:
    data = json.loads(line)

def map_user_to_redeem_offer(data):

    result = {}

    # filter out the unnecessary data
    events =[]
    cutoff = "2015-12-31 23:59:59"
    for event in data["events"]:
        if event["time"] <= cutoff:
            events.append(event)

    # sort the needed event data - no need to do this step
    # events.sort(key=lambda event:event["time"])

    # count for each user how many times each offer being used
    counts = {}
    for event in events:
        key = (event["user_id"], event["offer_id"])
        for offer in data["offers"]:
            if offer["offer_id"] != event["offer_id"]:
                continue
            if not (offer["start"] <= event["time"] <= offer["end"]):
                continue
            if event["type"] == "redeem":
                counts[key] = counts.get(key,0) + 1
            else:
                counts[key] = counts.get(key,0) - 1

    # go through offers dict and get the redeemable offer for each user
    users = set()
    for event in events:
        users.add(event["user_id"])

    for user in sorted(users):
        output_value = []
        for offer in data["offers"]:
            if offer["limit"] > counts.get((user,offer["offer_id"]),0) and offer["start"] <= cutoff <= offer["end"]:
                output_value.append(offer["offer_id"])
        result[user] = sorted(output_value)

    return result

'''

import csv
import sys

cutoff = "2015-12-31 23:59:59"

def solution():

    offers = {}
    counts = {}
    users = set()

    # parse csv file into offers
    reader = csv.DictReader(sys.stdin)

    for row in reader:
        if row["record_type"] == "OFFER":
            offers[row["name"]] = {
                "start_at" : row["start_at"],
                "end_at" : row["end_at"],
                "limit": int(row["user_max_redemption_count"])
            }
        # count for each user how many times each offer the user already used
        elif row["record_type"] == "EVENT":
            event_time = row["event_time"]
            user_id = row["user_id"]
            offer_name = row['offer_name']
            event_type = row["event_type"]

            users.add(user_id)

            if event_type != "REDEEM":
                continue

            if offer_name not in offers:
                continue

            offer = offers[offer_name]

            if not(offer["start_at"] <= event_time <= offer["end_at"]):
                continue

            key = (user_id,offer_name)
            counts[key] = counts.get(key,0) + 1

    # go through users and find the offers not exceed with the limit
    result = {}

    for user in users:
        result[user] = []

        for offer_name, offer in offers.items():

            if not(offer["start_at"] <= cutoff <= offer["end_at"]):
                continue

            count = counts.get((user, offer_name),0)

            if count < offer["limit"]:
                result[user].append(offer_name)

    # print the result dict
    for user in sorted(result):
        print(f"{user}: {','.join(sorted(result[user]))}")


solution()



