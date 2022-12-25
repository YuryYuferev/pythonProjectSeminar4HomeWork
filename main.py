# 1. Вычислить число pi c заданной точностью d
# Пример:   - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
# d = input('Введите степень округления в формате 0.01 от 10 в степени -1 до 10 в степени -10: ')
# d = d[2:len(d)]
# print(round(math.pi,len(d)))

# 2. Задай натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# a = int(input('Enter the number: '))
# list =[]
# for i in range(1, a+1):
#     if(a%i==0):
#       list.append(i)
# print(f'{a} = {list}')

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# import random
# k = int(input('Введите натуральную степень k: '))
# a = int(random.randint(0,100))
# b = int(random.randint(0,100))
# c = int(random.randint(0,100))
# if a != 0:
#     first = (str(a) + "x^" + str(k) + " + ")
# else:
#    first = (str())
# if b != 0:
#    second = (str(b) + "x" + " + ")
# else:
#    second = (str())
# if c != 0:
#    third = (str(c) + " = 0")
# else:
#    third = (str())
# print(f'{first}{second}{third}')

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# def add(A, B, m, n):
#     size = max(m, n)
#     sum = [0 for i in range(size)]
#     for i in range(0, m, 1):
#         sum[i] = A[i]
#     for i in range(n):
#         sum[i] += B[i]
#     return sum
# def printPoly(poly, n):
#     for i in range(n):
#         print(poly[i], end = "")
#         if (i != 0):
#             print("x^", i, end = "")
#         if (i != n - 1):
#             print(" + ", end = "")
# if __name__ == '__main__':
#     A = [6, 2, 10, 7]
#     B = [6, 5, 4]
#     m = len(A)
#     n = len(B)
#     print("Первый многочлен:")
#     printPoly(A, m)
#     print("\n", end = "")
#     print("Второй многочлен: ")
#     printPoly(B, n)
#     print("\n", end = "")
#     sum = add(A, B, m, n)
#     size = max(m, n)
#     print("Сумма многочленов:")
#     printPoly(sum, size)
