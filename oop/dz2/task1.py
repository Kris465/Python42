class Auto:
    def __init__(self, model, year, manufacturer, price):
        self.model = model
        self.__year = year
        self.manufacturer = manufacturer
        self.engine = input("Введите объем двигателя: ")
        self.__color = ""
        self.__price = price


    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def set_color(self):
        color = input("Введите цвет: ")
        self.__color = color

    def get_color(self):
        return self.__color

    def run(self):
        return "Машина едет"


class Huindai(Auto):
    def run(self):
        return "Huindai едет"


auto = Auto("Tank", "2023", "China", "200000")
print(auto.run())
auto1 = Huindai("I20", "2010", "Japan", "100000")
print(auto1.run())
