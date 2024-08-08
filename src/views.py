import datetime


def get_greeting(date_str: str) -> str:
    """Function get greeting from time"""

    time_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    greeting = ""
    if 6 <= time_obj.hour < 11:
        greeting = "Доброе утро"
    elif 11 <= time_obj.hour < 18:
        greeting = "Добрый день"
    elif 18 <= time_obj.hour < 23:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"

    return greeting


if __name__ == "__main__":
    print(get_greeting("2023-02-09 02:04:58"))
