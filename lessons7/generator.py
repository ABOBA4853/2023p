class Generator:
    def __init__(self, number=0):
        self.Number = number

    def Pow(self, pow):
        for i in range(1, pow + 1):
            yield self.Number ** i
