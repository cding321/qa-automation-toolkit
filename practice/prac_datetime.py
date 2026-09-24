from datetime import datetime

def solution(data):

    cutoff = datetime.strptime("2026-01-03 00:00:00","%Y-%m-%d %H:%M:%S")
    result = {}

    for s in data:
        txn_id, user_id, txn_time, amt = s.split("|")
        if datetime.strptime(txn_time, "%Y-%m-%d %H:%M:%S") >= cutoff:
            result[user_id] = result.get(user_id,0) + int(amt)

    for user_id, amt in sorted(result.items()):
            print(user_id, amt)
