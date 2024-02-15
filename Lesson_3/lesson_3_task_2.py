# Импортирую класс smartphone из файла user
from smartphone import Smartphone

# Создаю переменную catalog с типом список состоящую из пяти экземпляров класса Smartphone
catalog = [
    Smartphone("Siemens", "C-20", "+7-999-888-7711"),
    Smartphone("Nokia", "A320", "+7-999-777-5522"),
    Smartphone("Sony", "T-100", "+7-999-777-5533"),
    Smartphone("Motorolla", "C90", "+7-999-777-5544"),
    Smartphone("LG", "asd123", "+7-999-777-5555")
]

# Перебираю список в цикле и печатаю его в формате <марка> - <модель>. <номер телефона>.
for i in catalog:
    print(f"{i.phone} - {i.model}. {i.number}")