# Импортирую классы Address и Mailing из файлов address и mailing
from address import Address
from mailing import Mailing

# Создаю два экземпляра класса Address. Один содержит информацию откуда, второй куда
to_address = Address(101003, "Moscow", "Diribasovskay str.", "11", "22")
from_address = Address(125130, "New York", "Brighton Beach str.", "33", "44")

# Создаю два экземпляра класса Mailing. Принимающий на вход значения из экземпляров класса Address а также о стоимости и трек номер
mailing_instance = Mailing(to_address, from_address, 123, "12544806")

# Печатаю информацию о отправлении в 
# Использую формат: 
# Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> 
# в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей..
print(f"Отправление {mailing_instance.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.appartment} "
      f"в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.appartment}. "
      f"Стоимость {mailing_instance.cost} рублей.")
