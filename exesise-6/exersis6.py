from abc import ABC, abstractmethod

class Shape(ABC):

     @abstractmethod
     def area(self):
         pass 

     @abstractmethod
     def calculate_perimeter(self):
         pass 

class Rectangle(Shape):

     def __init__(self, width, height):

        self.width = width
        self.height = height

     def area(self):
        return self.width * self.height
     def calculate_perimeter(self):

        return 2 * (self.width + self.height) 

class Circle(Shape):
   def __init__(self, radius):
    self.radius = radius

   def area(self):
    pi = 3.14159 
    return pi * self.radius ** 2 


   def calculate_perimeter(self):
    pi = 3.14159 
    return 2 * pi * self.radius 

if __name__ == "__main__":


    shapes = [
     Rectangle(5, 3), 
                 Circle(4) 
]

    print("calculation area and perimeter of geometric shapes")
    
#
    for i, shape in enumerate(shapes, 1):
        print(f"\nshape{i}:")

    
        if isinstance(shape, Rectangle):

            print(f"rectangle,width: {shape.width}, height: {shape.height}")

        elif isinstance(shape, Circle):

           print(f"circle,radius: {shape.radius}")


    print(f"area: {shape.area():.2f}")
    print(f"perimeter: {shape.calculate_perimeter():.2f}")

   