import os

import pandas as pd
import requests
from pandas import DataFrame

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.xlsx")


def get_data_from_excel(excel_path: str) -> DataFrame:
    """Function get data from excel file."""

    if excel_path == "":
        excel_data = pd.DataFrame(
            {
                "Дата операции": [],
                "Дата платежа": [],
                "Номер карты": [],
                "Статус": [],
                "Сумма операции": [],
                "Валюта операции": [],
                "Сумма платежа": [],
                "Валюта платежа": [],
                "Кэшбэк": [],
                "Категория": [],
                "МСС": [],
                "Описание": [],
                "Бонусы (включая кэшбэк)": [],
                "Округление на инвесткопилку": [],
                "Сумма операции с округлением": [],
            }
        )
        return excel_data
    try:
        excel_data = pd.read_excel(excel_path)
        excel_data_no_nan = excel_data.loc[excel_data["Номер карты"].notnull()]
    except Exception:
        excel_data = pd.DataFrame()
        return excel_data
    return excel_data_no_nan


def get_currency_rates(currencies_list: list[str]) -> list[dict]:
    """Function get currency rates."""

    currency_rates = []
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    courses = response.json()
    for currency in currencies_list:
        currency_rates.append({"currency": currency, "price": courses["Valute"][currency]["Value"]})

    return currency_rates


def get_stock_rates(stocks: list[str], date="2024-08-08") -> list[dict]:
    """Function get stock rates."""

    stock_rates = []
    for stock in stocks:
        j = requests.get(f"https://iss.moex.com/iss/securities/{stock}/aggregates.json?date={date}").json()
        print(j)
        data = [{k: r[i] for i, k in enumerate(j["aggregates"]["columns"])} for r in j["aggregates"]["data"]]
        df_data = pd.DataFrame(data)
        try:
            price = round(float((df_data.loc[0, "value"] / df_data.loc[0, "volume"])), 2)
        except Exception:
            price = "не было торгов в этот день"
        stock_rates.append({"stock": stock, "price": price})
    return stock_rates
