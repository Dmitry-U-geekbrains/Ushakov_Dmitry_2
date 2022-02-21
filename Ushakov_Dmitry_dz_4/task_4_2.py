# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
from datetime import datetime
import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    if not (currency_code and url):
        return None
    currency_code = currency_code.upper()
    respond = requests.get(url)
    if respond.ok:
        cur = respond.text.split(currency_code)
        if len(cur) == 1:
            return None
        value = cur[1].split("</Value>")[0].split("<Value>")[1]
        value = float(value.replace(",", "."))
        date = respond.headers["Date"]
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
        return (value, date)
    else:
        return None


print((currency_rates("Usd")))
print((currency_rates("eUR")))
