import pandas as pd

def solution(df):
    '''
    df = pd.DataFrame({
        "user_id": ["U01", "U01", "U02", "U02", "U03"],
        "status": ["COMPLETED", "FAILED", "COMPLETED", "COMPLETED", "FAILED"],
        "amount": [100, 50, 200, 300, 400]
        })
    '''
    completed = df[df["status"]=="COMPLETED"]

    grouped = completed.groupby("user_id")

    result = grouped.agg(transaction_count=("amount","count"), total_amount=("amount","sum"))

    filtered = result[result["total_amount"] >= 300]

    sorted_result = filtered.sort_values("total_amount",ascending=False)

    return sorted_result



