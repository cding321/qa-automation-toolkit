import sys

sys.stdin = open("practice/input_test_a2.txt")

def solution():
    n = int(input())

    parent = {}

    for _ in range(n):
        line = input()
        business, children = line.split(",")

        for child in children.split("|"):
            parent[child] = business

    m = int(input())

    result = []

    for _ in range(m):
        line = input()
        loan_id, merchant, loan_amount = line.split(",")

        while merchant in parent:
            merchant = parent[merchant]

        # result.append([loan_id, merchant, loan_amount])
        print(f"{loan_id},{merchant},{loan_amount}")

    #return result


solution()