def get_high_value_users(payments,threshold):

    pm_list = set()
    res = {}
    lst = []

    for payment in payments:
        if payment['payment_id'] not in pm_list:
            pm_list.add(payment['payment_id'])
            if payment['status'] == "SUCCESS":
                user_id = payment['user_id']
                # res[x] = res.get(x,0) + payment['y'] -> group by x and sum y
                res[user_id] = res.get(user_id,0) + payment['amount']

    for i in res:
        if res[i] >= threshold:
            lst.append(i)

    return lst


print(get_high_value_users([
    {
        "payment_id": "p1",
        "amount": 100.0,
        "status": "FAILED"
    },
    {
        "payment_id": "p1",
        "amount": 100.0,
        "status": "SUCCESS"
    }
],90))

print(get_high_value_users([
    {"payment_id": "p1", "user_id": "u1", "amount": 100.0, "status": "SUCCESS"},
    {"payment_id": "p2", "user_id": "u1", "amount": 50.0, "status": "FAILED"},
    {"payment_id": "p3", "user_id": "u2", "amount": 25.0, "status": "SUCCESS"},
    {"payment_id": "p1", "user_id": "u1", "amount": 100.0, "status": "SUCCESS"},
    {"payment_id": "p4", "user_id": "u2", "amount": 75.0, "status": "SUCCESS"},
],90))