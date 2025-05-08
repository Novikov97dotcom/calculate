# Geometric Shapes Library

Библиотека для вычисления площади геометрических фигур и выполнения различных операций с ними.

## Функциональность

- Вычисление площади круга по радиусу
- Вычисление площади треугольника по трем сторонам
- Проверка, является ли треугольник прямоугольным
- Легкость добавления новых типов фигур через наследование
- Вычисление площади фигуры без знания типа фигуры в compile-time

## Примеры использования

### Круг

```python
from shapes import Circle

# Вычисление площади круга
circle = Circle(5)
print(circle.area())  # 78.53981633974483
```

### Треугольник

```python
from shapes import Triangle

# Вычисление площади треугольника
triangle = Triangle(3, 4, 5)
print(triangle.area())  # 6.0

# Проверка, является ли треугольник прямоугольным
print(triangle.is_right())  # True
```

### Вычисление площади без знания типа фигуры

```python
from shapes import Circle, Triangle, calculate_area

# Создаем фигуры
circle = Circle(5)
triangle = Triangle(3, 4, 5)

# Вычисляем площадь, не зная тип фигуры в compile-time
shapes = [circle, triangle]
for shape in shapes:
    print(calculate_area(shape))
# Выводит:
# 78.53981633974483
# 6.0
```

## Расширение библиотеки

Для добавления новой фигуры необходимо:

1. Наследоваться от базового класса `Shape`
2. Реализовать метод `area()` для вычисления площади

Пример добавления новой фигуры (прямоугольник):

```python
from shapes import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
``` 