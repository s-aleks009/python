"""Запуск программы

"""

from CreateSheet import CreateSheet

CreateSheet("USD/RUB тейк", "USDT", "take").start_ss()
CreateSheet("USD/RUB мейк", "USDT", "make").start_ss()
CreateSheet("BTC/RUB тейк", "BTC", "take").start_ss()
CreateSheet("BTC/RUB мейк", "BTC", "make").start_ss()
