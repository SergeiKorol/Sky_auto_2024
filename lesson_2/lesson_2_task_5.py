# Задание 5. Месяц — сезон

# Создаю функцию month_to_season  принимающую на вход число номер месяца

def month_to_season(month_num):
    if month_num in (1, 2, 12):
        season = 'Зима'
    elif month_num in (3, 4, 5):
        season = 'Весна'
    elif month_num in (6, 7, 8):
        season = 'Лето'
    elif month_num in (9, 10, 11):
        season = 'Осень'
    else: season = 'Введено число > 12'
    return season

# Вызываю функцию 
month_num = int(input("Введите номер месяца "))
print('Время года:', month_to_season(month_num))