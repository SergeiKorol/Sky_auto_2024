# Задание 6. Создание функции
# Объявить функцию print_greeting() и вызвать её

# 1 вариант
def print_greeting_1():
    print("Привет, мир!")


print_greeting_1()


# 2 вариант локальная область видимости
def print_greeting_2():
    text = input()
    print(text)


# 3 вариант глобальная область видимости
text = input()


def print_greeting_3():
    print(text)


print_greeting_3()


# 4 вариант параметр
def print_greeting_4(param):
    print(param)


print_greeting_4("Привет, мир!")
