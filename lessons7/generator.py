class Generator:
    def __init__(self, number = 0):
        self.Number = number
    def __call__(self, val):
        self.Number = val
        return f"Val: {self.Number}"
    def __str__(self):
        return f"Number: {self.Number}"
    def Pow(self, pow):
        for i in range(1, pow+1):
            yield self.Number ** i