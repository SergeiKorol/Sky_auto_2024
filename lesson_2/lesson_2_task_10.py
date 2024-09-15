# Задание 10. Банковское приложение

# Создаю функцию bank, принимающую аргументы deposit и years
# функция возвращающает сумму, которая будет на счету пользователя спустя years лет.
def bank(deposit, years):
    if years > 0:
        for i in range(1, years + 1):
            deposit = deposit * 1.1
        return deposit
    else:
        return deposit


# Получаю пользовательский ввод
deposit = int(input("Введите сумму депозита = "))
years = int(input("Введите срок вклада = "))

# Вызываю функцию
print('Сумма на депозите спустя', years, 'лет', 'составит:', bank(deposit, years))
