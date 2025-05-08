"""Shapes module for geometric calculations."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.
        
        Returns:
            float: The area of the shape
        """
        pass


class Circle(Shape):
    """Class representing a circle shape."""

    def __init__(self, radius):
        """Initialize a circle with the given radius.
        
        Args:
            radius (float): The radius of the circle
            
        Raises:
            ValueError: If radius is not positive
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        """Calculate the area of the circle.
        
        Returns:
            float: The area of the circle
        """
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """Class representing a triangle shape."""

    def __init__(self, side_a, side_b, side_c):
        """Initialize a triangle with three sides.
        
        Args:
            side_a (float): Length of the first side
            side_b (float): Length of the second side
            side_c (float): Length of the third side
            
        Raises:
            ValueError: If any side is not positive or if sides can't form 
                a triangle
        """
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("All sides must be positive")
            
        # Check triangle inequality
        if (side_a + side_b <= side_c or 
                side_a + side_c <= side_b or 
                side_b + side_c <= side_a):
            raise ValueError("The given sides cannot form a triangle")
            
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        """Calculate the area of the triangle using Heron's formula.
        
        Returns:
            float: The area of the triangle
        """
        # Semi-perimeter
        s = (self.side_a + self.side_b + self.side_c) / 2
        
        # Heron's formula
        return math.sqrt(s * (s - self.side_a) * 
                         (s - self.side_b) * (s - self.side_c))

    def is_right(self):
        """Check if the triangle is a right triangle using Pythagorean theorem.
        
        Returns:
            bool: True if the triangle is a right triangle, False otherwise
        """
        # Sort sides to make checking easier
        sides = sorted([self.side_a, self.side_b, self.side_c])
        
        # Check Pythagorean theorem: a² + b² = c²
        # Using a small epsilon for floating-point comparison
        epsilon = 1e-9
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < epsilon


def calculate_area(shape):
    """Calculate the area of any shape.
    
    Args:
        shape (Shape): A shape object implementing the Shape interface
        
    Returns:
        float: The area of the shape
        
    Raises:
        TypeError: If shape is not a Shape instance
    """
    if not isinstance(shape, Shape):
        raise TypeError("Expected a Shape instance")
    return shape.area() 