import os

import pandas as pd
from pandas import DataFrame

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.xlsx")


def get_data_from_excel(excel_path: str) -> DataFrame:
    """Function get data from excel file."""

    if excel_path == '':
        excel_data = pd.DataFrame({'Дата операции': [],
                       'Дата платежа': [],
                       'Номер карты': [],
                       'Статус': [],
                       'Сумма операции': [],
                       'Валюта операции': [],
                       'Сумма платежа': [],
                       'Валюта платежа': [],
                       'Кэшбэк': [],
                       'Категория': [],
                       'МСС': [],
                       'Описание': [],
                       'Бонусы (включая кэшбэк)': [],
                       'Округление на инвесткопилку': [],
                       'Сумма операции с округлением': []
                      })
        return excel_data
    try:
        excel_data = pd.read_excel(excel_path)
    except Exception:
        excel_data = pd.DataFrame()
    return excel_data


if __name__ == "__main__":
#     print(get_data_from_excel(os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests", "test_operations.xlsx")))
    print(get_data_from_excel(''))
    empty_df = pd.DataFrame({'Дата операции': [],
                       'Дата платежа': [],
                       'Номер карты': [],
                       'Статус': [],
                       'Сумма операции': [],
                       'Валюта операции': [],
                       'Сумма платежа': [],
                       'Валюта платежа': [],
                       'Кэшбэк': [],
                       'Категория': [],
                       'МСС': [],
                       'Описание': [],
                       'Бонусы (включая кэшбэк)': [],
                       'Округление на инвесткопилку': [],
                       'Сумма операции с округлением': []
                      })
    print(bool(empty_df == get_data_from_excel('')))
