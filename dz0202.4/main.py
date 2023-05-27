
from triangle import Triangle
from rectangle import Rectangle
from ball import Ball
from calculate import CalculateArea
triangle = Triangle(10, 17)
rectangle = Rectangle(5, 10)
square = Rectangle(5)
ball = Ball(13)
area = CalculateArea()
print(f"Area of triangle {area.TriangleArea(triangle)}")
print(f"Area of rectangle {area.RectangleArea(rectangle)}")
print(f"Area of square {area.RectangleArea(square, True)}")
print(f"Area of ball {area.BallArea(ball)}")

