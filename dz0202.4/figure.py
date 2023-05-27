from idlelib.multicall import r


class Figure:
    def __init__(self, width = 0, length = 0, R=13):
        self.Width = width
        self.Length = length
        self.R = r
    def __str__(self):
        return f'Width = {self.Width}\n' \
               f'Length = {self.Length}\n' \
               f'Length = {self.R}\n' \
               f'Call base str:\t{super().__str__()}'


