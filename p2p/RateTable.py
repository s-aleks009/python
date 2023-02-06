from exchanges.GetBinance import GetBinance
from exchanges.GetHuobi import GetHuobi
from exchanges.GetKucoin import GetKucoin


class RateTable:
    """Запуск парсеров, сбор курсов в список

    Take: Купить - buy, Продать - sell
    Make: Купить - sell, Продать - buy

    """

    def __init__(self, crypto):
        self.crypto = crypto
        if crypto == "USDT":
            self.crypto_huobi = 2
        elif crypto == "BTC":
            self.crypto_huobi = 1
        self.header = [
            "",
            "Binance Тинькофф",
            "Binance QIWI",
            "Binance ЮMoney",
            "Kucoin",
            "Huobi Тинькофф",
            "Huobi Сбер",
            "Huobi ВТБ",
            "Huobi QIWI",
            "Huobi ЮMoney",
            # "Bitzlato Тинькофф",  РКН
            # "Bitzlato Сбер",  РКН
            # "Bitzlato ВТБ",   РКН
            # "Bitzlato Мир",   РКН
            # "Bitzlato QIWI",  РКН
            # "Bitzlato ЮMoney" РКН
        ]
        self.buy = [
            "Купить",
            GetBinance(self.crypto, "RUB", "Tinkoff", "BUY").get_rate(),
            GetBinance(self.crypto, "RUB", "QIWI", "BUY").get_rate(),
            GetBinance(self.crypto, "RUB", "YandexMoney", "BUY").get_rate(),
            GetKucoin(self.crypto, "RUB", "SELL").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 28, "sell").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 29, "sell").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 27, "sell").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 9, "sell").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 19, "sell").get_rate()
            # GetBitzlato(self.crypto, "RUB", "purchase", "443").get_rate(),
            # # Tinkoff
            # GetBitzlato(self.crypto, "RUB", "purchase", "3547").get_rate(),
            # # sber
            # GetBitzlato(self.crypto, "RUB", "purchase", "446").get_rate(),
            # # vtb
            # GetBitzlato(self.crypto, "RUB", "purchase", "1114").get_rate(),
            # # mir
            # GetBitzlato(self.crypto, "RUB", "purchase", "444").get_rate(),
            # # qiwi
            # GetBitzlato(self.crypto, "RUB", "purchase", "8975").get_rate()
            # # yandex
        ]
        self.sell = [
            "Продать",
            GetBinance(self.crypto, "RUB", "Tinkoff", "SELL").get_rate(),
            GetBinance(self.crypto, "RUB", "QIWI", "SELL").get_rate(),
            GetBinance(self.crypto, "RUB", "YandexMoney", "SELL").get_rate(),
            GetKucoin(self.crypto, "RUB", "BUY").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 28, "buy").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 29, "buy").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 27, "buy").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 9, "buy").get_rate(),
            GetHuobi(self.crypto_huobi, 11, 19, "buy").get_rate()
            # GetBitzlato(self.crypto, "RUB", "selling", "443").get_rate(),
            # # Tinkoff
            # GetBitzlato(self.crypto, "RUB", "selling", "3547").get_rate(),
            # # sber
            # GetBitzlato(self.crypto, "RUB", "selling", "446").get_rate(),
            # # vtb
            # GetBitzlato(self.crypto, "RUB", "selling", "1114").get_rate(),
            # # mir
            # GetBitzlato(self.crypto, "RUB", "selling", "444").get_rate(),
            # # qiwi
            # GetBitzlato(self.crypto, "RUB", "selling", "8975").get_rate()
            # # yandex
        ]

    def get_rates_tbl_take(self):
        return [self.header, self.buy, self.sell]

    # Для мейкера надо поменять местами buy и sell
    def get_rates_tbl_make(self):
        return [self.header, self.sell, self.buy]
