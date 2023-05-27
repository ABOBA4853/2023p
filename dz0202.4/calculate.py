from triangle import Triangle
from rectangle import Rectangle
from ball import math
class CalculateArea:
    def RectangleArea(self, rectangle = Rectangle(), isSquare = False):
        if(rectangle.Width != 0):
            if(not isSquare and rectangle.Length != 0):
                return rectangle.Width * rectangle.Length
            return rectangle.Width * 2
    def TriangleArea(self, triangle = Triangle()):
        if(triangle.Width != 0 and triangle.Length != 0):
            return 0.5 * triangle.Width * triangle.Length

    def BallArea(self, R):
        print(4 * math.pi * R ** 2)

    def BallVolume(self, R):
        print(4 / 3 * math.pi * pow(R, 3))


