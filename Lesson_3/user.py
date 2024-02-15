# Задание 1. Создание класса

# Объявляю класс User
class User:
    # Создаю конструктор класса принимающий на вход 3 параметра
    def __init__(self, first_name, last_name):     
        # Присваиваю значения полям класса  User 
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name

    # Создаю методы класса
    def say_name(self):
        print("Моё имя", self.first_name)
    def say_last_name(self):
        print("Моя фамилия" , self.last_name)
    def say_full_name(self):
        print("Моё полное ФИО", self.full_name)