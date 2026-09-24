import sys

# sys.stdin = open("practice/input_test_a2.txt")

'''
def solution():
    with open("practice/input_test_a2.txt") as f:
        n = int(f.readline())

        # n = int(input())

        parent = {}

        for _ in range(n):
            # line = input()
            line = f.readline().strip()
            business, children = line.split(",")

            for child in children.split("|"):
                parent[child] = business

        # m = int(input())
        m = int(f.readline())

        result = []

        for _ in range(m):
            # line = input()
            line = f.readline().strip()
            loan_id, merchant, loan_amount = line.split(",")

            while merchant in parent:
                merchant = parent[merchant]

            # result.append([loan_id, merchant, loan_amount])
            print(f"{loan_id},{merchant},{loan_amount}")

        #return result


solution()


def solution_2(relationship,customer_loans):
    parent = {}

    for company, children in relationship.items():
        for child in children:
            parent[child] = company

    result = []

    for loan in customer_loans:
        company = loan["loan_company"]

        while company in parent:
            company = parent[company]
            result.append(
                {
                    "customer":loan["customer"],
                    "topmost_parent": company
                }
         )

    return result


solution_2({'AA': ['BB','CC'],'DD': ['AA']},{'customer': 'customer1', 'loan_company': 'CC'})
'''


def solution_3():
    with open("practice/input_test_a2_2.txt") as f:
        c,l = f.readline().split()
        parent_tree = {}
        for _ in range(c):
            line = f.readline().strip()
            child, parent = line.split()
            if parent != "None":
                parent_tree[child] = parent

        grouping = {}
        for _ in range(l):
            line = f.readline().strip()
            loan_id, company = line.split()

            while company in parent_tree:
                company = parent_tree[company]

            if company not in grouping:
                grouping[company] = []

            grouping[company].append(loan_id)

        for root in sorted(grouping):
            print(f"{root}:{' '.join(grouping[root])}")
