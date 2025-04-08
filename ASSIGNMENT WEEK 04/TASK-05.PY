'''
5. You need to create a system where multiple shapes (like Circle,
Rectangle, and Triangle) can be drawn using a common method,
showcasing polymorphism.
• Create a base class Shape with a method draw().
• Create three subclasses: Circle, Rectangle, and Triangle. Each
subclass should override the draw() method to display a unique
message.
• Write a function draw_shape(shape) that takes a Shape object and
calls its draw() method.
• Create instances of each shape and call draw_shape() on them.


'''
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle!")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle!")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle!")

def draw_shape(shape):
    shape.draw()

circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

draw_shape(circle)
draw_shape(rectangle)
draw_shape(triangle)
