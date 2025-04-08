'''
2. Create abstract base class "shape" that has abstract method "area".
Inherit rectangle, triangle and square class from shape class and provide
implementation of "area" method for each derived class. Finally print
area of rectangle, triangle and square.
'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def __str__(self):
        return f"Name: {self.name} , Area: {self.area()}"
    
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.name = "Rectangle"
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    
    
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.name = "Triangle"
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    

class Square(Shape):
    def __init__(self, side):
        self.name = "Square"
        self.side = side
        
    def area(self):
        return self.side ** 2
    
    
    
rectangle = Rectangle(4, 5)
triangle = Triangle(3, 6)
square = Square(4)


print(rectangle)  
print(triangle)   
print(square) 
    
    