import pytest
from utils.data_summary import summarize_results


# @pytest.fixture
# def sample_results():
#     return ["PASS", "FAIL", "PASS", "ERROR"]



@pytest.mark.parametrize(
    "data, expected",
    [
        pytest.param(
            ["PASS", "FAIL", "PASS", "ERROR"],
            {"PASS":2, "FAIL":1, "ERROR":1},
            id="normal_case"
        ),
        pytest.param(
            [],
            {},
            id="empty_list"
        ),
        pytest.param(
            ["PASS"],
            {"PASS":1},
            id="single_result"
        ),
    ],
)

def test_summarize_results(data, expected):

    assert summarize_results(data) == expected


@pytest.mark.parametrize(
    "data",
    [
        pytest.param("PASS", id="string_input"),
        pytest.param(123, id="integer_input"),
        pytest.param(None, id="none_input"),
    ]
)

def test_summarize_invalid_input(data):

    with pytest.raises(TypeError, match="results must be a list"):
        summarize_results(data)


@pytest.mark.xfail(
    reason="empty list handling is not implemented yet",
    strict=True
)
def test_empty_list_new_requirement():
    assert summarize_results([]) == {"EMPTY": 0}