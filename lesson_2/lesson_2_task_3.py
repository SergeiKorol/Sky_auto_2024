# Задание 3. Площадь квадрата
import math 

# Создаю функцию square принимающую на вход сторону квадрата
def square(square_side):
  square_area = square_side * square_side 
  return math.ceil(square_area) 

# Привожу к числу пользовательский ввод и вызываю функцию
square_side = float(input("Введите сторону квадрата "))
print("Площадь квадрата = ", square(square_side))
