import pytest
from src.views import get_greeting, get_data_about_cards, get_top_transactions


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


def test_get_data_about_cards(test_operations):
    assert get_data_about_cards(test_operations) == [{"last digits": "*7197", "total_spent": 224.89, "cashback": 2.25}]


def test_get_top_transactions(top_5):
    assert get_top_transactions(top_5, 2) == [{'date': '31.12.2019', 'amount': 17000, 'category': 'Услуги банка', 'description': 'Колхоз'}, {'date': '31.12.2020', 'amount': 4575.45, 'category': 'Фастфуд', 'description': 'Колхоз'}]
