import requests
import json
from statistics import mean


class GetBybit:
    """Получение курса Bybit

    """

    def __init__(self, token, currency, payment, side):
        self.token = token
        self.currency = currency
        self.payment = payment
        self.side = side
        self.url = "https://api2.bybit.com/spot/api/otc/item/list"
        self.lst_price = []

    def data(self):
        data = {
            "userId": "",
            "tokenId": self.token,
            "currencyId": self.currency,
            "payment": self.payment,
            "side": self.side,
            "size": 10,
            "page": 1,
            "amount": ""
        }
        return data

    def headers(self):
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU",
            "Content-Length": "76",
            "Content-type": "application/x-www-form-urlencoded",
            "guid": "cdeec2d5-b567-76dd-9817-614c20a19a05",
            "lang": "ru - RU",
            "Origin": "https://www.bybit.com",
            "platform": "PC",
            "referer": "https://www.bybit.com/",
            "sec-ch-ua": "' Not;A Brand';v='99', 'Microsoft Edge';v='103', 'Chromium';v='103'",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44 "
        }
        return headers

    def get_rate(self):
        try:
            print(self.data())
            response = requests.post(self.url, headers=self.headers(),
                                    data=self.data())

            page = response.text
            print(page)
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

GetBybit("USDT", "RUB", 75, 0).get_rate()
