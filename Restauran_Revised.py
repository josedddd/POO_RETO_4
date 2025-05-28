
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
        for menu_item, quantity in self.order:
            price = menu_item.calculate_price(quantity)
            total_quantity += quantity
            if menu_item.name == "Hamburger" and isinstance(menu_item, Beverage):
                price *= 0.9
                total_bill += price
            elif menu_item.name == "Fried chicken" and isinstance(menu_item, Dessert):
                price *= 0.95
                total_bill += price
            elif menu_item.name == "Coca-cola" and  isinstance(menu_item, MainPlate):
                price *= 0.87
            total_bill += menu_item.calculate_price(quantity)
        if total_quantity >= 10:
            total_bill *= 0.97
        return total_bill


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
            
# 🥤 Drinks
coca = Beverage("Coca-cola", 2.5)
coca.set_size("medium")
coca.set_bottle_type("plastic")

agua = Beverage("Water", 1.5)
agua.set_size("large")
agua.set_bottle_type("glass")

jugo = Beverage("Orange juice", 3.0)
jugo.set_size("small")
jugo.set_bottle_type("tetra pak")

te = Beverage("Iced tea", 2.0)
te.set_size("medium")
te.set_bottle_type("plastic")

# 🍟 Apetizer
papas = Apetizer("French fries", 3.0)
papas.set_sauce("Ketchup")

alitas = Apetizer("Wings", 4.5)
alitas.set_sauce("BBQ")

nuggets = Apetizer("Nuggets", 3.5)
nuggets.set_sauce("Mustard")

ensalada = Apetizer("Mixed salad", 3.0)
ensalada.set_sauce("Ranch")

# 🍽️ Main Course
hamburguesa = MainPlate("Hamburger", 6.0)
hamburguesa.set_accompaniment1("French fries")
hamburguesa.set_accompaniment2("Salad")

pollo_frito = MainPlate("Fried chicken", 7.0)
pollo_frito.set_accompaniment1("Mashed potatoes")
pollo_frito.set_accompaniment2("Corn")

lasaña = MainPlate("Lasagna", 8.0)
lasaña.set_accompaniment1("Garlic bread")
lasaña.set_accompaniment2("Green salad")

bistec = MainPlate("Steak", 9.5)
bistec.set_accompaniment1("Rice")
bistec.set_accompaniment2("Sautéed potatoes")

# 🍰 Dessert
helado = Dessert("Ice cream", 2.0)
helado.set_flavour("Vanilla")

pastel = Dessert("Chocolate cake", 2.5)
pastel.set_flavour("Chocolate")

flan = Dessert("Flan", 2.2)
flan.set_flavour("Caramel")

brownie = Dessert("Brownie", 2.8)
brownie.set_flavour("Walnut")


# Create an order
orden_1 = Order(number=1)

# Add items
orden_1.add_items(hamburguesa, 2)     # Hamburger (MainPlate)
orden_1.add_items(jugo, 2)            # Juice (Beverage)
orden_1.add_items(nuggets, 2)         # Nuggets (Apetizer)
orden_1.add_items(helado, 2)          # Ice cream (Dessert)
orden_1.add_items(agua, 2)            # Water (Beverage)


# Calculate total price, there is a 10% in beverage, because the item hamburger 
total = orden_1.calculate_total_price()
print(total)

# Add the payment
pago_efectivo = Money_Payment(total)
pago_efectivo.set_amount(50.0)  # The customer gives $50
print(pago_efectivo.pay())


