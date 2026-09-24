import json

def solution(file):
    data = json.load(file)
    result = {}

    for row in data:
        user_id = row["user_id"]
        amt = row["amount"]
        if row["status"] == "COMPLETED":
            result[user_id] = result.get(user_id,0) + amt

    for user_id, amt in sorted(result.items()):
        if amt >= 100:
            print(user_id, amt)