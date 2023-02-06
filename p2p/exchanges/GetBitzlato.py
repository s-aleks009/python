import requests
import json
from statistics import mean


class GetBitzlato:
    """Получение курса Bitzlato

    """

    def __init__(self, crypto, currency, type, paymethod):
        self.crypto = crypto
        self.currency = currency
        self.type = type
        self.paymethod = paymethod
        self.url = "https://bitzlato.com/api2/p2p/public/exchange/dsa/"
        self.lst_price = []

    def data(self):
        data = {
            "skip": 0,
            "limit": 15,
            "cryptocurrency": self.crypto,
            "currency": self.currency,
            "type": self.type,
            "isOwnerVerificated": "true",
            "isOwnerTrusted": "false",
            "isOwnerActive": "false",
            "paymethod": self.paymethod,
            "lang": "ru"
        }
        return data

    def get_rate(self):
        try:
            response = requests.get(self.url, params=self.data())

            page = response.text
            lst_price = self.lst_price
            # Переводим str в dict
            d = json.loads(page)

            # Получаем список объявлений из data
            # В каждом объявлении ищем значение для ключа 'rate'
            for i in d['data']:
                lst_price.append(i['rate'])

            lst_price = [float(x) for x in lst_price]
            rate = mean(lst_price[:5])
            print(
                f"Bitzlato-{self.crypto}-{self.currency}-{self.type}-{self.paymethod}"
                f": Complete :-)")
            return rate
        except OSError:
            rate = 0
            print(
                f"Bitzlato-{self.crypto}-{self.currency}-{self.type}-{self.paymethod}"
                f": ERROR!!! (URL)")
            return rate
        except KeyError:
            rate = 0
            print(
                f"Bitzlato-{self.crypto}-{self.currency}-{self.type}-{self.paymethod}"
                f": ERROR!!! (Структура JSON)")
            return rate
