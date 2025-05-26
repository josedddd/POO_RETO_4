
class Shape():
    def __init__(self):
        pass
    def compute_perimeter(self):
        pass
    def compute_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__()
        self.width=width
        self.height=height

    def compute_area(self) -> float:
        area = self.width * self.height
        return area

    def compute_perimeter(self) -> float:
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

class Square(Shape):
    def __init__(self, width):
        super().__init__()
        self.width=width


    def compute_area(self) -> float:
        area = self.width **2
        return area

    def compute_perimeter(self) -> float:
        perimeter = 4 * self.width
        return perimeter
### Ejemplo de uso    
Square1=Square(width=4)
Rectangle1=Rectangle(width=5,height=4)
print(Rectangle1.compute_area)
print(Square1.compute_area())
print(Rectangle1.compute_perimeter())
print(Square1.compute_perimeter())
