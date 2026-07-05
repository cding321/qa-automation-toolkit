def summarize_results(result):
    summary = {}

    for r in result:
        summary[r] = summary.get(r,0) + 1

    return summary

if __name__ == '__main__':
    data = ["PASS", "FAIL", "SKIP", "ERROR", "PASS"]
    print(summarize_results(data))