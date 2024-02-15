# Задание 3. Вложенные классы

# Объявляю класс Address
class Address:
    # Создаю конструктор класса принимающий на вход 6 параметров
    def __init__(self, _index, _city, _street, _house, _appartment):
        # Присваиваю значения полям класса Address 
        self.index = _index
        self.city = _city
        self.street = _street
        self.house = _house
        self.appartment = _appartment
