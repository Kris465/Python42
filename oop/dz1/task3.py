class Stadion:
    def __init__(self, title, country, city):
        self.title = title
        self.date = input("Введите дату: ")
        self.country = country
        self.city = city
        self.__countity = ""
        
        def set_countity(self):
            countity = input("Введите страну: ")
            self.__countity = countity
        
        def get_countity(self):
            return self.__countity

 
stadion = Stadion("Roma", "USA", "Hollywood")
print(stadion.title, stadion.city, stadion.country)
        


