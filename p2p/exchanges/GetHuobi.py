import requests
import json
from statistics import mean, StatisticsError


class GetHuobi:
    """Получение курса GetHuobi

    """

    def __init__(self, coinId, currency, payMethod, tradeType):
        self.coinId = coinId
        self.currency = currency
        self.payMethod = payMethod
        self.tradeType = tradeType
        self.url = "https://otc-api.bitderiv.com/v1/data/trade-market"
        self.lst_price = []

    def data(self):
        data = {
            "coinId": self.coinId,
            "currency": self.currency,
            "tradeType": self.tradeType,
            "currPage": 1,
            "payMethod": self.payMethod,
            "acceptOrder": 0,
            "country": "",
            "blockType": "general",
            "online": 1,
            "range": 0,
            "amount": "",
            "onlyTradable": "false"
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
                lst_price.append(i['price'])

            lst_price = [float(x) for x in lst_price]
            rate = mean(lst_price[:5])
            print(
                f"Huobi-{self.coinId}-{self.currency}-{self.payMethod}-{self.tradeType}"
                f": Complete :-)")
            return rate
        except OSError:
            rate = 1
            print(
                f"Huobi-{self.coinId}-{self.currency}-{self.payMethod}-{self.tradeType}"
                f": ERROR!!! (URL)")
            return rate
        except KeyError:
            rate = 1
            print(
                f"Huobi-{self.coinId}-{self.currency}-{self.payMethod}-{self.tradeType}"
                f": ERROR!!! (Структура JSON)")
            return rate
        except StatisticsError:
            rate = 1
            print(
                f"Huobi-{self.coinId}-{self.currency}-{self.payMethod}-{self.tradeType}"
                f": ERROR!!! (Мало предложений)")
            return rate
