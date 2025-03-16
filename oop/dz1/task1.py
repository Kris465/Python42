class Auto:
    def __init__(self, model, year, manufacturer, color, price):
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


auto = Auto("Tesla", "2015", "Musk", "White", "100000")
print(auto.model, auto.manufacturer, auto.engine)

auto.set_color()
print(auto.get_year(), auto.get_color(), auto.get_price())
