# Импортирую класс User из файла user
from user import User

# Создаю экземпляр класса User
my_user = User("Ivan","Ivanov")

# Вызываю методы класса User из экземпляра класса
my_user.say_name()
my_user.say_last_name()
my_user.say_full_name()