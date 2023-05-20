from triangle import Triangle
from rectangle import Rectangle
class CalculateArea:
    def RectangleArea(self, rectangle = Rectangle(), isSquare = False):
        if(rectangle.Width != 0):
            if(not isSquare and rectangle.Length != 0):
                return rectangle.Width * rectangle.Length
            return rectangle.Width * 2
    def TriangleArea(self, triangle = Triangle()):
        if(triangle.Width != 0 and triangle.Length != 0):
            return 0.5 * triangle.Width * triangle.Length