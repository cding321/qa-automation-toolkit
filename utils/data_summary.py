def summarize_results(results):

    if not isinstance(results, list):
        raise TypeError("results must be a list")

    summary = {}

    for r in results:
        summary[r] = summary.get(r,0) + 1

    return summary

if __name__ == '__main__':
    data = ["PASS", "FAIL", "SKIP", "ERROR", "PASS"]
    print(summarize_results(data))