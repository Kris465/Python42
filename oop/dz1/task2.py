class Book:
    def __init__(self, booktitle, publisher, genre, author, price):
        self.booktitle = booktitle
        self.year = input("Введите год выпуска: ")
        self._publisher = ""
        self.genre = genre
        self._author = author
        self._price = price

    def set_publisher(self):
        publisher = input("Введите название издательства: ")
        self._publisher = publisher

    def get_publisher(self):
        return self._publisher

    def get_author(self):
        return self._author

    def get_price(self):
        return self._price

book = Book("Idiot", "Moscow", "Roman", "Dostoevsky", "1000")
print(book.booktitle, book.year, book.genre)

book.set_publisher()
print(book.get_publisher(), book.get_author(), book.get_price())
