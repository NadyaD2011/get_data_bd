from dotenv import load_dotenv

import requests
import os


def get_holidays(url, key):
    params = {
        'api_key': key,
        'year': 2025,
        'country': 'ru'
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    holidays = response.json()['response']['holidays']

    return holidays


def write_result(holidays):
    months = [
        'Января',
        'Февраля',
        'Марта',
        'Апреля',
        'Мая',
        'Июня',
        'Июля',
        'Августа',
        'Сентября',
        'Октября',
        'Ноября',
        'Декабря'
    ]

    for holiday in holidays:
        index_month = holiday["date"]['datetime']['month']-1
        print(f'Дата: {holiday["date"]['datetime']['day']} {months[index_month]}\nНазвание праздника: {holiday["name"]}\nОписание: {holiday["description"]}\n')


def main():
    load_dotenv()

    url = 'https://calendarific.com/api/v2/holidays'
    key = os.getenv("API_KEY")

    holidays = get_holidays(url, key)

    write_result(holidays)


if __name__ == "__main__":
    main()
