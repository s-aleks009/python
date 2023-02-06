class PercentTable:
    """Рассчёт процентов спреда

    ((sell - buy)/buy) * 100

    """

    def __init__(self, crypto, rates_tbl):
        self.crypto = crypto
        self.rates_tbl = rates_tbl
        self.percent_tbl = []

    def get_percent_tbl(self):
        return [
            [(((s - b) / b) * 100) for b in self.rates_tbl[1] if type(b) != str]
            for s in self.rates_tbl[2] if type(s) != str]
