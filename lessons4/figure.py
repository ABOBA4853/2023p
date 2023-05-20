class Figure:
    def __init__(self, width = 0, length = 0):
        self.Width = width
        self.Length = length
    def __str__(self):
        return f'Width = {self.Width}\n' \
               f'Length = {self.Length}\n' \
               f'Call base str:\t{super().__str__()}'


