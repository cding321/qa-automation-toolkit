#import json
#import sys
#for line in sys.stdin:
#    data = json.loads(line)

def map_user_to_redeem_offer(data):

    result = {}

    # filter out the unnecessary data
    events =[]
    cutoff = "2015-12-31 23:59:59"
    for event in data["events"]:
        if event["time"] <= cutoff:
            events.append(event)

    # sort the needed event data
    events.sort(key=lambda event:event["time"])

    # count for each user how many times each offer being used
    counts = {}
    for event in events:
        key = (event["user_id"], event["offer_id"])
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




