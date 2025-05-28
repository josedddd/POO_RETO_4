# POO_RETO_4

Aqui explicare todo lo que se hizo.
# Punto1
Comenzando por el punto 1 del ejercicio en clase, este era simplemente realizar una superclase Shape de la que solo hereda rectangulo y cuadrado solamente para probar el polimorfismo, aqui no hay mucho de que comentar :).

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
# Punto2
Ahora bien, con respecto al segundo ejercicio la cosa se vuelve mas interesante. En este se pedia realizar en codigo el diagrama UML, que aparecia en el reto. Primero decidi de utilizar los vertices, para calcular las otras cosas por lo que set(edges) esta como compute(edges). Luego cree la "super clase" Shape, donde defino todas las funciones que se utilizaran. Cable aclarar que puse todos los atributos de tipo protegido y no privado, puesto que nescecito que se herede despues (PD no cree setter ni getter para la clase Point, ni la clase Line, pero es que no es nescecario): 

```python
  
class Shape():
    def __init__(self):
        pass

    def set_is_regular(self, is_regular:bool):
        self._is_regular=is_regular

    def get_is_regular(self):
        return self._is_regular

    def set_vertices(self, vertices:list):
        self._vertices=vertices

    def get_vertices(self) -> list:
        return [(self._vertices[x].x, self._vertices[x].y) for x in range(len(self._vertices))]
    
    def compute_edges(self):
        pass

    def get_edges(self):
        pass

    def compute_inner_angles(self):
        pass        

    def compute_perimeter(self):
        pass

    def compute_area(self):
        pass
```
En consiguiente creo la clase rectangulo. Es muy importante tener en cuenta el orden de meter los vertices, pues esto cambia mucho el codigo (se podria arreglar con manejar errores pero eso no se ha viso :/). Asimismo en la funcion compute_inner_angles, realmente no los calculo, pero es que los angulos de un rectangulo siempre son 90, asi que no veo ninguna nescecidad (si me dio un poco de pereza), luego creo la clase square y al heredo de rectangulo. Una ultima cosa es que antes de lo que esta en get_edges, llamo la funcion compute_edges, puesto que si no se ha llamado esta antes, se va a generar un error

```python

class Rectangle(Shape):

    def __init__(self):
        super().__init__()
    
    def compute_edges(self):   
        #Estructura de vertices de un rectangulo: 
        #[point_left_up, point_right_up, point_right_down, point_left_dowm]
        self._edgeH_up = Line(self._vertices[0], self._vertices[1])
        self._edgeH_down = Line(self._vertices[3], self._vertices[2])
        self._edgeV_left = Line(self._vertices[0], self._vertices[3])
        self._edgeV_right = Line(self._vertices[1], self._vertices[2])

    def get_edges(self) -> list:
        self.compute_edges()
        return [
            {
                "name": "top edge",
                "start": (self._edgeH_up.point_start.x, self._edgeH_up.point_start.y),
                "end": (self._edgeH_up.point_end.x, self._edgeH_up.point_end.y),
                "length": self._edgeH_up.compute_length()
            },
            {
                "name": "bottom edge",
                "start": (self._edgeH_down.point_start.x, self._edgeH_down.point_start.y),
                "end": (self._edgeH_down.point_end.x, self._edgeH_down.point_end.y),
                "length": self._edgeH_down.compute_length()
            },
            {
                "name": "left edge",
                "start": (self._edgeV_left.point_start.x, self._edgeV_left.point_start.y),
                "end": (self._edgeV_left.point_end.x, self._edgeV_left.point_end.y),
                "length": self._edgeV_left.compute_length()
            },
            {
                "name": "right edge",
                "start": (self._edgeV_right.point_start.x, self._edgeV_right.point_start.y),
                "end": (self._edgeV_right.point_end.x, self._edgeV_right.point_end.y),
                "length": self._edgeV_right.compute_length()
            }
        ]

    def compute_area(self) -> float:
        self.compute_edges()
        return (self._edgeH_up.compute_length()*self._edgeV_right.compute_length() 
       
    def compute_perimeter(self) -> float:
        self.compute_edges()
        return 2*self._edgeH_up.compute_length()+2*self._edgeV_right.compute_length()
    
    def compute_inner_angles(self):
        return [90, 90, 90, 90]
```
En consiguiente creo la clase trianguo. Aqui no es tan nescecario tener en cuenta el orden de los vertices. Uso la ley de coseno y la ley del area universal de los triangulos para calcular el area y los angulos internos (si esta vez si los calculo). 
```python
class Triangle(Shape):

    def __init__(self):
        super().__init__()

    def compute_edges(self): 
        ## Orden de colocar los vertices 
        # [Vertice superior, Vertice_inferior derecho, Vertice inferior izquierdo]
        
        self._edge1 = Line(self._vertices[0], self._vertices[1])
        self._edge2 = Line(self._vertices[1], self._vertices[2])
        self._edge3 = Line(self._vertices[2], self._vertices[0])
        self._leng_edge1= self._edge1.compute_length()
        self._leng_edge2= self._edge2.compute_length()
        self._leng_edge3= self._edge3.compute_length()


    def get_edges(self):
        self.compute_edges()
        return [
        {
            "name": "A",
            "start": (self._edge1.point_start.x, self._edge1.point_start.y),
            "end": (self._edge1.point_end.x, self._edge1.point_end.y),
            "length": self._leng_edge1
        },
        {
            "name": "B",  
            "start": (self._edge2.point_start.x, self._edge2.point_start.y),
            "end": (self._edge2.point_end.x, self._edge2.point_end.y),
            "length": self._leng_edge2
        },
        {
            "name":"C",
            "start": (self._edge3.point_start.x, self._edge3.point_start.y),
            "end": (self._edge3.point_end.x, self._edge3.point_end.y),
            "length": self._leng_edge3
        }
    ]

    def compute_inner_angles(self):
        self.compute_edges
         #### El orden del calculo de los angulos es 
         # [Angulo opuesto al lado "A", Angulo opuesto al Lado B, Angulo opuesto al lado C]
        self.compute_edges()
        cos_angle_edge1= (self._leng_edge3**2 + self._leng_edge2**2 - self._leng_edge1**2) / (
            2 * self._leng_edge3* self._leng_edge2)
        self.angle_edge_1 = degrees(acos(cos_angle_edge1))
        cos_angle_edge2 = (self._leng_edge3**2 + self._leng_edge1**2 - self._leng_edge2**2) / (
            2 * self._leng_edge3* self._leng_edge1)
        self.angle_edge_2 = degrees(acos(cos_angle_edge2))
        cos_angle_edge3 = (self._leng_edge2**2 + self._leng_edge1**2 - self._leng_edge3**2) / (
            2 * self._leng_edge2* self._leng_edge1)
        self.angle_edge_3 = degrees(acos(cos_angle_edge3))
       
        return[self.angle_edge_1, self.angle_edge_2, self.angle_edge_3]
        
    def compute_area(self) -> float:
        self.compute_edges()
        self.compute_inner_angles()
        return (1/2*self._leng_edge1*self._leng_edge2*sin(radians(self.angle_edge_3)))
       
    def compute_perimeter(self) -> float:
        self.compute_edges()
        return (self._leng_edge1+self._leng_edge2 +self._leng_edge3)
```
Por ultimo heredo todas los tipos de triangulo (como use ley de coseno y el area universal, esas funciones sirven pa todo tipo de triangulo, ( el punto de orientacion de objetos es reutilizar codigo no?) 
```python
class EquilateralTriangle(Triangle):

    def __init__(self):
        super().__init__()
    
class IsoscelesTriangle(Triangle):
     def __init__(self):
        super().__init__()

class ScaleneTriangle(Triangle):
    def __init__(self):
        super().__init__()

class RightTriangle(Triangle):
    def __init__(self):
        super().__init__()
```
# Restaurante
Lo que cambio en el restaurante es uno, le puse setter y getter a las subclases de Menu_Item y ademas puse Menu_Item en protegido (no en privado)
```python

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_price(self, quantity: int) -> float:
        return self.price * quantity
    
    
class Beverage(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
  
    def set_size(self, size:str):
        self.__size = size

    def get_size(self:str):
        return self.__size

    def set_bottle_type(self, bottle_type):
        self.__bottle_type = bottle_type

    def get_bottle_type(self):
        return self.__bottle_type

    def with_ice(self, answer) -> str:
        if answer == "yes":
            return f"your {self.name} is with ice"
        elif answer == "no":
            return f"your {self.name} is without ice"


class Apetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def set_sauce(self, sauce:str):
        self.__sauce = sauce

    def get_sauce(self):
        return self.__sauce


class Dessert(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def set_flavour(self, flavour:str):
        self.__flavour = flavour

    def get_flavour(self):
        return self.__flavour


class MainPlate(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def set_accompaniment1(self, accompaniment_1:str):
        self.__accompaniment1 = accompaniment_1

    def get_accompaniment1(self):
        return self.__accompaniment1

    def set_accompaniment2(self, accompaniment_2:str):
        self.__accompaniment2 = accompaniment_2

    def get_accompaniment2(self):
        return self.__accompaniment2

```
Ahora bien, tambien le hice una modificacion para que si detecta tal item, me haga descuento en todos los otros items de una clase, esto lo primero haciendo una lista con todos los nombres, y luego en un for haciendo que si tal item esta en nombres entonces aplicame descuentos en tal clase. Esto se hace usando la funcion de python Isistance la cual detecta si un objeto pertence a cierta clase,(No juzgar los descuentos, fue lo primero que se me vino a la mente)
```python

class Order:
    def __init__(self, number):
        self.number = number
        self.order = []

    def add_items(self, menu_item: MenuItem, quantity: int) -> list:
        self.order.append((menu_item, quantity))

    def show_order(self) -> list:
        return [f"{item.name}, {quantity}" for item, quantity in self.order]

    def calculate_total_price(self) -> float:
        total_bill = 0
        total_quantity = 0
        main_plate_names = []
        
        for item, quantity in self.order:
            if isinstance(item, MainPlate):
                main_plate_names.append(item.name)

        for menu_item, quantity in self.order:
            price = menu_item.calculate_price(quantity)

            if "Hamburger" in main_plate_names and isinstance(menu_item, Beverage):
                price *= 0.9  # 10% Discount on beverages

            if "Fried chicken" in main_plate_names and isinstance(menu_item, Dessert):
                price *= 0.95  # 5% Discount on desserts

            total_bill += price
            total_quantity += quantity

        if total_quantity >= 10:
            total_bill *= 0.97  # 3% discount if the order has 10 items or more

        return total_bill
```
Por ultimo añadi los payment methods, tal como se vio en clase, usando poliformismo para variar el metodo pay dependiendo si se paga en efectivo o con tarjeta y ya eso es todo.

```python

class Payment:
    def __init__(self, bill):
        self.bill = bill

    def pay(self):
        pass


class Card_Payment(Payment):
    def __init__(self, bill):
        super().__init__(bill)
       
    def set_number_card(self, number_card: str):
        self.__number_card = number_card
    
    def set_cvv(self, cvv: int):
        self.__cvv = cvv
    
    def pay(self):
        return f"Thanks for paying {self.bill} with the card ending with {self.__number_card[-4:]}"


class Money_Payment(Payment):
    def __init__(self, bill):
        super().__init__(bill)
     
    def set_amount(self, amount: float):
        self.__amount = amount
    
    def get_amount(self):
        return self.__amount
    
    def pay(self):
        if self.__amount >= self.bill:
            return f"Thanks for paying {self.bill}, here is your change {self.__amount - self.bill}"
        else:
            return "You don't have enough money :///"

```

