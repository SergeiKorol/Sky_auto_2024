# Задание 4. FizzBuzz. Задачка с собеседования

# Создаю функцию fizz_buzz принимающую на вход число n 
# Перебираю в цикле числа от 1 до n и проверяю их на делимость на 3 и 5
def fizz_buzz(n):
    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
           print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)

n = int(input('Введите число n = '))
fizz_buzz(n)
