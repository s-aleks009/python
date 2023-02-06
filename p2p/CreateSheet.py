from google_api.connection_to_google import *
import datetime
import spreadsheet_id
from RateTable import RateTable
from PercentTable import PercentTable


class CreateSheet:
    """Создание листа с курсами

    """

    def __init__(self, name, crypto, process):
        self.name = name
        self.crypto = crypto
        self.rates = RateTable(self.crypto)
        if process == "take":
            self.rates_tbl = self.rates.get_rates_tbl_take()
        elif process == "make":
            self.rates_tbl = self.rates.get_rates_tbl_make()
        self.percent_tbl = PercentTable(self.crypto,
                                        self.rates_tbl).get_percent_tbl()
        self.current_date_time = datetime.datetime.now()
        self.spreadsheetId = spreadsheet_id.spreadsheetId

    def start_ss(self):
        service.spreadsheets().values().clear(spreadsheetId=self.spreadsheetId,
                                              range='{0}!A1:Z'.format(self.name),
                                              body={}).execute()
        service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheetId, body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": self.name + "!A1:B1",  # Заголовок листа
                     "majorDimension": "ROWS",
                     "values": [
                         [self.name,
                          self.current_date_time.strftime('%d.%m.%Y %H:%M:%S')]
                     ]},
                    {"range": self.name + "!A2:C20",  # Таблица курсов
                     "majorDimension": "COLUMNS",
                     "values": self.rates_tbl},
                    {"range": self.name + "!F2:F20",  # Шапка таблицы процентов
                     "majorDimension": "COLUMNS",
                     "values": [self.rates_tbl[0]]},
                    {"range": self.name + "!F2:Z2",  # Шапка таблицы процентов
                     "majorDimension": "ROWS",
                     "values": [self.rates_tbl[0]]},
                    {"range": self.name + "!E3",  # Купить (таблица процентов)
                     "majorDimension": "ROWS",
                     "values": [["Купить"]]},
                    {"range": self.name + "!G1",  # Продать (таблица процентов)
                     "majorDimension": "ROWS",
                     "values": [["Продать"]]},
                    {"range": self.name + "!G3:Z20",  # Таблица процентов
                     "majorDimension": "COLUMNS",
                     "values": self.percent_tbl}
                ]
            }).execute()

        print(f"{self.name}: OK")
