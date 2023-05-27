class Human:

    def __init__(self, name = None, isWinner = False):
        self.Name = name
        self.isWinner = isWinner

    def __str__(self):
        return self.Name


