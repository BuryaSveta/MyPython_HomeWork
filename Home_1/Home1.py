# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

# day = int(input('Введите день: '))
# if day == 1:
#     print('Понедельник')
# elif day == 2:
#     print('Вторник')
# elif day == 3:
#     print('Среда')
# elif day == 4:
#     print('Четверг')
# elif day == 5:
#     print('Пятница')
# elif day == 6:
#     print('Суббота')
# else:
#     print('Воскресенье')
# if day > 7 or day < 1:
#     print('Нет такого дня!')


# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,1
# A (7,-5); B (1,-1) -> 7,21

# import math

# x1 = float(input('Введите координату точки А по оси Х: '))
# y1 = float(input('Введите координату точки А по оси Y: '))
# x2 = float(input('Введите координату точки B по оси Х: '))
# y2 = float(input('Введите координату точки B по оси Y: '))

# distance = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
# print(distance)
