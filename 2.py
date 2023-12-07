class Book:

    def __init__(self, author, title, price):
        if not isinstance(author, str):
            raise TypeError
        if not isinstance(title, str):
            raise TypeError
        if not isinstance(price, int):
            raise TypeError
        if price < 0:
            raise ValueError
        self.__author = author
        self.__title = title
        self.__price = price

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, int):
            raise TypeError
        if new_price < 0:
            raise ValueError
        self.__price = new_price


class Order:

    def __init__(self, client_name: str, client_email: str):
        if not isinstance(client_name, str):
            raise TypeError
        if not isinstance(client_email, str):
            raise TypeError
        if "@" not in client_email:
            raise ValueError
        self.__client_name = client_name
        self.__client_email = client_email
        self.__book = []

    def add(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError
        self.__book.append(book)

    def remove(self, title: str):
        if not isinstance(title, str):
            raise TypeError
        for index, book in enumerate(self.__book):
            if book.title == title:
                self.__book.pop(index)

    @property
    def client_name(self):
        return self.__client_name

    @client_name.setter
    def client_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError
        self.__client_name = new_name

    @property
    def client_email(self):
        return self.__client_email

    @client_email.setter
    def client_email(self, new_email):
        if not isinstance(new_email, str):
            raise TypeError
        if "@" not in new_email:
            raise ValueError
        self.__client_email = new_email

    @property
    def count(self):
        return len(self.__book)

    @property
    def price(self):
        all_price = 0
        for book in self.__book:
            all_price += book.price
        return all_price