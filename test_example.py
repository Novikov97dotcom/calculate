"""Example usage of the shape_area_calculator module."""
from shape_area_calculator import Circle, Triangle, calculate_area

circle = Circle(5)
print(calculate_area(circle))  # Вывод: 78.53981633974483 (это площадь круга с радиусом 5)

triangle = Triangle(3, 4, 5)
print(calculate_area(triangle))  # Вывод: 6.0 (площадь треугольника со сторонами 3, 4, 5)
print(triangle.is_right_triangle())  # Вывод: True (треугольник прямоугольный) 