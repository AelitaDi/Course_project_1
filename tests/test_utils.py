import os
from unittest.mock import patch

import pandas as pd
from src.utils import get_data_from_excel, get_currency_rates, get_stock_rates


@patch("src.utils.pd.read_excel")
def test_get_data_from_excel(mock_read_excel, empty_df):
    mock_read_excel.return_value = empty_df
    assert get_data_from_excel("test.xlsx").equals(empty_df)
    mock_read_excel.assert_called_once_with("test.xlsx")


@patch("requests.get")
def test_get_currency_rates(mock_get):
    mock_get.return_value.json.return_value = {"Valute": {"EUR": {"Value": 95.1844}}}
    assert get_currency_rates(["EUR"]) == [{'currency': 'EUR', 'price': 95.1844}]
    mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")


@patch("requests.get")
def test_get_stock_rates(mock_get, moex_response):
    mock_get.return_value.json.return_value = moex_response
    assert get_stock_rates(["YDEX"]) == [{"stock": "YDEX", "price": 4.0}]
    mock_get.assert_called_once_with("https://iss.moex.com/iss/securities/YDEX/aggregates.json?date=2024-08-08")
