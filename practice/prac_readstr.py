import sys

def solution_multi_line_str(data):
    '''
    data = """U01|John Smith|COMPLETED|100
              U02|Alice Lee|FAILED|200
              U03|Bob Chen|COMPLETED|150
              U01|John Smith|COMPLETED|50"""

    data.splitlines() = 
    [
    "U01|John Smith|COMPLETED|100",
    "U02|Alice Lee|FAILED|200",
    "U03|Bob Chen|COMPLETED|150",
    "U01|John Smith|COMPLETED|50"
    ]
    '''
    result = {}
    for s in data.splitlines():
        user_id, name, status, amount = s.split("|")
        if status == "COMPLETED":
            result[user_id] = result.get(user_id,0) + float(amount)

    for user_id, amount in sorted(result.items()):
        if amount >= 100:
            print(user_id, amount)


def solution_list(data):
    '''
    data = [
        "U01|John Smith|COMPLETED|100",
        "U02|Alice Lee|FAILED|200",
        "U03|Bob Chen|COMPLETED|150",
        "U01|John Smith|COMPLETED|50"
    ]
    '''
    result = {}
    for s in data:
        user_id, name, status, amount = s.split("|")
        if status == "COMPLETED":
            result[user_id] = result.get(user_id, 0) + float(amount)

    for user_id, amount in sorted(result.items()):
        if amount >= 100:
            print(user_id, amount)


def solution_sys_stdin():
    result = {}
    for s in sys.stdin:
        user_id, name, status, amount = s.strip().split("|")
        if status == "COMPLETED":
            result[user_id] = result.get(user_id,0) + float(amount)

    for user_id, amount in sorted(result.items()):
        if amount >= 100:
            print(user_id, amount)


def solution_zip(data):
    '''
    data = [
        "user_id|name|status|amount",
        "U01|John Smith|COMPLETED|100",
        "U02|Alice Lee|FAILED|200",
        "U03|Bob Chen|COMPLETED|150"
    ]
    '''
    header = data[0]
    headers = header.split("|")
    '''
    headers = ["user_id", "name", "status", "amount"]
    '''
    result = {}
    for s in data[1:]:
        values = s.split("|")
        '''
        first values = ["U01","John Smith","COMPLETED","100"]
        '''
        row = dict(zip(headers,values))
        '''
        row = 
        {
            "user_id": "U01",
            "name": "John Smith",
            "status": "COMPLETED",
            "amount": "100"
        }
        '''
        user_id = row["user_id"]
        amount = row["amount"]
        status = row["status"]
        if status == "COMPLETED":
            result[user_id] = result.get(user_id,0) + int(amount)

    for user_id, amount in sorted(result.items()):
        if amount >= 100:
            print(user_id, amount)



