# Задание 2. Високосный год

# Создаю функцию is_year_leap принимающую на вход год
def is_year_leap(year):
    if year % 4 == 0:
         return True
    else:
        return False

# Вызываю функцию
year = int(input("Введите год для проверки високосности "))
print(f'год {year}:', is_year_leap(year))

