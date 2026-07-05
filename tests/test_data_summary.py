from utils.data_summary import summarize_results

def test_summarize_results():
    data = ["PASS","FAIL","PASS","ERROR"]

    expected = {
        "PASS":2,
        "FAIL":1,
        "ERROR":1
    }

    assert summarize_results(data) == expected


def test_empty_list():
    data = []
    expected = {}
    assert summarize_results(data) == expected


def test_single_value():
    data = ["PASS"]
    expected = {"PASS":1}
    assert summarize_results(data) == expected


