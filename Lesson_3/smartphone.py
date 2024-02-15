# Задание 2. Список объектов

# Объявляю класс Smartphone
class Smartphone:
    # Создаю конструктор класса принимающий на вход 4 параметра
    def __init__(self, _phone, _model, _number):
        # Присваиваю значения полям класса Smartphone
        self.phone = _phone
        self.model = _model
        self.number = _number
        