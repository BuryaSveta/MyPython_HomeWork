# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Введите число N: '))
# factorial = 1
# for i in range(1, N+1):
#     factorial *= i
#     print(factorial, end =', ')

#Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

# print("x | y | z | ¬(X ∧ Y) ∨ Z")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             print(f"{x} | {y} | {z} | {int(not (x and y) or z)}")


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

# str1 = input('Введите текст 1: ')
# str2 = input('Введите текст 2: ')

# for symbol in set(str1):
#     print(symbol,'-',str2.count(symbol))
