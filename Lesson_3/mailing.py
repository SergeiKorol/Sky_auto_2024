# Объявляю класс Mailing
class Mailing:
    # Создаю конструктор класса принимающий на вход 5 параметров
    def __init__(self, _to_address, _from_address, _cost, _track ):
        # Присваиваю значения полям класса Mailing
        self.to_address = _to_address
        self.from_address = _from_address
        self.cost = _cost
        self.track = _track
