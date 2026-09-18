from prac_tech_a2 import solution


def test_normal_case(monkeypatch):
    test_input = [
        "2",
        "ByteDance International,TikTok USDS|ByteDance North America",
        "ByteDance North America,TikTok|TikTok Store",
        "4",
        "L1,TikTok Store,100.00",
        "L2,TikTok,50.00",
        "L3,ByteDance North America,75.00",
        "L4,Unknown Merchant,20.00"
    ]

    monkeypatch.setattr("builtins.input", lambda: test_input.pop(0))

    result = solution()

    expected = [
        "L1,ByteDance International,100.00",
        "L2,ByteDance International,50.00",
        "L3,ByteDance International,75.00",
        "L4,Unknown Merchant,20.00"
    ]

    assert result == expected