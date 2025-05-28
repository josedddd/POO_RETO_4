# POO_RETO_4

Aqui explicare todo lo que se hizo. Comenzando por el punto 1 del ejercicio en clase, este era simplemente realizar una superclase Shape de la que solo hereda rectangulo y cuadrado solamente para probar el polimorfismo, aqui no hay mucho de que comentar :).

```python
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
```
Ahora bien, con respecto al segundo ejercicio la cosa se vuelve mas interesante. En este se pedia realizar en codigo el diagrama UML, que aparecia en el reto. Primero decidi de utilizar los vertices, para calcular las otras cosas por lo que set(edges) esta como compute(edges). Luego cree la "super clase" Shape


