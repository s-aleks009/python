import requests
import json
from statistics import mean


class GetBinance:
    """Получение курса Binance

    """

    def __init__(self, asset, fiat, pay, trade):
        self.asset = asset
        self.fiat = fiat
        self.pay = pay
        self.trade = trade
        self.url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
        self.lst_price = []

    def data(self):
        data = {
            "asset": self.asset,
            "countries": [],
            "fiat": self.fiat,
            "page": 1,
            "payTypes": [self.pay],
            "publisherType": None,
            "rows": 10,
            "tradeType": self.trade
        }
        return data

    def headers(self):
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "Content-Length": "125",
            "Content-type": "application/json",
            "Origin": "https://p2p.binance.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44 "
        }
        return headers

    def get_rate(self):
        try:
            response = requests.post(self.url, headers=self.headers(),
                                     json=self.data())

            page = response.text
            lst_price = self.lst_price
            # Переводим str в dict
            d = json.loads(page)

            # Получаем список объявлений из data
            # В каждом объявлении входим в словарь 'adv'.
            # В нём ищем значение для ключа 'price'
            for i in d['data']:
                lst_price.append(i['adv']['price'])

            lst_price = [float(x) for x in lst_price]
            rate = mean(lst_price[:5])
            print(
                f"Binance-{self.asset}-{self.fiat}-{self.pay}-{self.trade}"
                f": Complete :-)")
            return rate
        except OSError:
            rate = 0
            print(
                f"Binance-{self.asset}-{self.fiat}-{self.pay}-{self.trade}"
                f": ERROR!!! (URL)")
            return rate
        except KeyError:
            rate = 0
            print(
                f"Binance-{self.asset}-{self.fiat}-{self.pay}-{self.trade}"
                f": ERROR!!! (Структура JSON)")
            return rate
