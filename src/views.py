import datetime
import os
from collections import Counter

import pandas as pd
from pandas import DataFrame

from src.utils import get_data_from_excel

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.xlsx")


def get_greeting(date_str: str) -> str:
    """Function get greeting by time."""

    time_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    if 6 <= time_obj.hour < 11:
        greeting = "Доброе утро"
    elif 11 <= time_obj.hour < 18:
        greeting = "Добрый день"
    elif 18 <= time_obj.hour < 23:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"

    return greeting


def get_data_about_cards(df_data: DataFrame) -> list[dict]:
    """Function get data about user cards from DataFrame."""

    cards_list = list(Counter(df_data.loc[:, "Номер карты"]))
    cards_data = []
    for card in cards_list:
        j_df_data = df_data.loc[df_data.loc[:, "Номер карты"] == card]
        total_spent = abs(sum(j for j in j_df_data.loc[:, "Сумма операции"] if j < 0))
        cashback = round(total_spent / 100, 2)
        cards_data.append({"last digits": card, "total_spent": total_spent, "cashback": cashback})
    return cards_data


def get_top_transactions(df_data: DataFrame, top_number=5) -> list[dict]:
    """Function get top-5 transactions from DataFrame."""

    top_transactions_list = []
    df_data["amount"] = df_data["Сумма платежа"].map(float).map(abs)
    sorted_df_data = df_data.sort_values(by="amount", ascending=False, ignore_index=True)
    for i in range(top_number):
        date = sorted_df_data.loc[i, "Дата платежа"]
        amount = sorted_df_data.loc[i, "amount"]
        category = sorted_df_data.loc[i, "Категория"]
        description = sorted_df_data.loc[i, "Описание"]
        top_transactions_list.append(
            {"date": date, "amount": amount, "category": category, "description": description}
        )
    return top_transactions_list


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "Дата платежа": ["31.12.2021", "31.12.2021", "31.12.2020", "31.12.2019", "31.12.2018"],
            "Сумма операции": ["-160.89", "-64.0", "-4575.45", "-17000.0", "-5.05"],
            "Сумма платежа": ["-160.89", "-64", "-4575.45", "-17000", "-5.05"],
            "Категория": ["Супермаркеты", "Супермаркеты", "Фастфуд", "Услуги банка", "Переводы"],
            "Описание": ["Колхоз", "Колхоз", "Колхоз", "Колхоз", "Колхоз"],
        }
    )

    # print(get_greeting("2023-02-09 02:04:58"))
    df_ = get_data_from_excel(PATH_TO_FILE)

    print(get_top_transactions(df))
    # print(get_top_transactions(df_))
