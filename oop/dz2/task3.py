class Stadion:
    def __init__(self, name, country, city):
        self.name = name
        self.country = country
        self.city = city
        self.capacity = input("Введите вместимость стадиона: ")

    def play(self):
        return "Сегодня футбольный матч"


class Vympel(Stadion):
    def match(self):
        return "Сегодня игра по теннису"


stadion = Stadion("Metallist", "RF", "Korolyov")
print(stadion.play(), stadion.name)

stadion1 = Vympel("Main Stadion", "RF", "Korolyov")
print(stadion1.match(), stadion1.name)
