import requests
import json
from statistics import mean


class GetKucoin:
    """Получение курса Kucoin

    """

    def __init__(self, currency, legal, side):
        self.currency = currency
        self.legal = legal
        self.side = side
        self.url = "https://www.kucoin.com/_api/otc/ad/list"
        self.lst_price = []

    def data(self):
        data = {
            "currency": self.currency,
            "side": self.side,
            "legal": self.legal,
            "page": 1,
            "pageSize": 10,
            "status": "PUTUP",
            "lang": "ru_RU"
        }
        return data

    def get_rate(self):
        try:
            response = requests.get(self.url, params=self.data())

            page = response.text
            lst_price = self.lst_price

            # Переводим str в dict
            d = json.loads(page)

            # Получаем список объявлений из items
            # В каждом объявлении ищем значение для ключа 'floatPrice'
            for i in d['items']:
                lst_price.append(i['floatPrice'])

            lst_price = [float(x) for x in lst_price]
            rate = mean(lst_price[:5])
            print(
                f"Kucoin-{self.currency}-{self.legal}-{self.side}"
                f": Complete :-)")
            return rate
        except OSError:
            rate = 0
            print(
                f"Kucoin-{self.currency}-{self.legal}-{self.side}"
                f": ERROR!!! (URL)")
            return rate
        except KeyError:
            rate = 0
            print(
                f"Kucoin-{self.currency}-{self.legal}-{self.side}"
                f": ERROR!!! (Структура JSON)")
            return rate
