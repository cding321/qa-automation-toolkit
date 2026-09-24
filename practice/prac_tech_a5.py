def find_users():
    day1_user = set()
    day2_user = set()

    n,m = map(int,input().split())

    for _ in range(n):
        user_id, loan_type = map(int,input().split())
        if loan_type >= 2:
            day1_user.add(user_id)

    for _ in range(m):
        user_id, loan_type = map(int, input().split())
        if loan_type >= 2:
            day2_user.add(user_id)

    result = sorted(day1_user & day2_user)

    print(*result)



