from figure import Figure
class Ball(Figure):
    def __init__(self, R):
        super().__init__(R)
    def area(self, R):
        print(4 * math.pi * R ** 2)
    def volume(self, R):
        print(4 / 3 * math.pi * pow(R, 3))