# Задание 2. Високосный год

# Создаю функцию is_year_leap принимающую на вход год
def is_year_leap(year):
    if year % 4 == 0:
         return True
    else:
        return False

# Проверяю что функция правильно определяет високосный год или нет 2024 - високосный, 2023 не високосный
print('Год 2023:', is_year_leap(2023))
print('Год 2024:', is_year_leap(2024))