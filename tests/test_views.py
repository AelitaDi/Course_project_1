import pytest
from src.views import get_greeting


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("2023-01-01 06:05:04", "Доброе утро"),
        ("2023-01-01 13:05:04", "Добрый день"),
        ("2023-01-01 20:05:04", "Добрый вечер"),
        ("2023-01-01 01:05:04", "Доброй ночи"),
    ],
)
def test_get_greeting(input_data, expected):
    assert get_greeting(input_data) == expected
