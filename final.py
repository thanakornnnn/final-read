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

class Hero:
    def __init__(self, name, max_hp=100):
        self.__name = name
        self.__hp = self.__max_hp = max_hp
        self.__alive = True

    def __process_damage(self, damage):
        """ Update the damage value here before it gets subtracted from HP.
            For example, reduce it to apply defense, or divide it to apply
            damage resistance (50% damage, etc.). """
        return damage

    def attack(self, target):
        if self.__alive:
            target.take_hit(self.attack_value)

    def take_hit(self, damage):
        if self.__alive:
            self.__hp -= self.__process_damage(damage)
        if self.__hp <= 0:
            self.__hp = 0
            self.__alive = False

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def max_hp(self):
        return self.__max_hp

    def __str__(self):
        return f"{self.__name}: {self.__class__.__name__} {self.__hp}/{self.__max_hp}"


class Warrior(Hero):

    def __init__(self, name, max_hp=120, str=10):
        Hero.__init__(self, name, max_hp)
        self.__str = str
        self.__attack_value = self.__str*2

    @property
    def str(self):
        return self.__str

    @property
    def attack_value(self):
        return self.__attack_value

    def __process_damage(self, damage):
        return damage * 0.5


class Wizard(Hero):

    def __init__(self, name, max_hp=60, wis=5):
        Hero.__init__(self, name, max_hp)
        self.__wis = wis
        self.__attack_value = self.__wis*2

    @property
    def wis(self):
        return self.__wis

    @property
    def attack_value(self):
        return self.__attack_value

    def __process_damage(self, damage):
        return damage - 5


class Hero:
    def __init__(self, name, max_hp=100):
        self.__name = name
        self.__hp = self.__max_hp = max_hp
        self.__alive = True

    def __process_damage(self, damage):
        """ Update the damage value here before it gets subtracted from HP.
            For example, reduce it to apply defense, or divide it to apply
            damage resistance (50% damage, etc.). """
        return damage

    def attack(self, target):
        if self.__alive:
            target.take_hit(self.attack_value)

    def take_hit(self, damage):
        if self.__alive:
            self.__hp -= self.__process_damage(damage)
        if self.__hp <= 0:
            self.__hp = 0
            self.__alive = False

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def max_hp(self):
        return self.__max_hp

    def __str__(self):
        return f"{self.__name}: {self.__class__.__name__} {self.__hp}/{self.__max_hp}"


class Warrior(Hero):

    def __init__(self, name, max_hp=120, str=10):
        Hero.__init__(self, name, max_hp)
        self.__str = str
        self.__attack_value = self.__str*2

    @property
    def str(self):
        return self.__str

    @property
    def attack_value(self):
        return self.__attack_value

    def __process_damage(self, damage):
        return damage * 0.5


class Wizard(Hero):

    def __init__(self, name, max_hp=60, wis=5):
        Hero.__init__(self, name, max_hp)
        self.__wis = wis
        self.__attack_value = self.__wis*2

    @property
    def wis(self):
        return self.__wis

    @property
    def attack_value(self):
        return self.__attack_value

    def __process_damage(self, damage):
        return damage - 5
Collapse
chao5_1.py
2 KB
class VendingMachine:

    def __init__(self, price, capacity):
        if not isinstance(price, int):
            raise TypeError("Price must be integer type")
        self.__price = price

class VendingMachine:

    def __init__(self, price, capacity):
        if not isinstance(price, int):
            raise TypeError("Price must be integer type")
        self.__price = price
        if not isinstance(capacity, int):
            raise TypeError("Capacity must be integer type")
        self.__capacity = capacity
        self.__money = 0
        self.__drinks = 0
        self.__power = False

    @property
    def money(self):
        return self.__money

    @property
    def drinks(self):
        return self.__drinks

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, set_power):
        if not isinstance(set_power, bool):
            raise TypeError("Power must be boolean type")
        self.__power = set_power

    def sell(self):
        if not self.__power:
            raise ValueError("There is no power")
        if self.__drinks == 0:
            raise ValueError("There is no drinks")
        self.__money += self.__price
        self.__drinks -= 1

    def refill(self, amount=None):
        if amount > self.__capacity:
            raise ValueError("Can't go above capacity")
        if self.__power:
            raise ValueError("Power is still one")
        if amount is None:
            self.__drinks = self.__capacity
        else:
            self.__drinks = amount

    def maintenance_mode(self):
        self.__money = 0
        self.__drinks = 0
        self.__power = False
