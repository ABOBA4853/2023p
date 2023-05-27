class LimitError(Exception):
    def __init__(self, amount = 0, limit = 0):
        self.Amout = amount
        self.Limit = limit
    def __str__(self):
        return f'Dear customer we have only {self.Limit} selected goods by you\n' \
                f'but you want {self.Amout} goods\n' \
                f'Please wait for goods 2 days.'