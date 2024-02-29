import math as m
#Найти самый часто встречающийся символ в строке. Если несколько вывести любой
#Самое оптимальное решение
# s = input()
# dct = {}
# ans = ''
# anscnt = 0
# for now in s:
#     if now not in dct:
#         dct[now] = 0
#     dct[now] += 1
# for key in dct:
#     if dct[key] > anscnt:
#         anscnt = dct[key]
#         ans = key
# print(f'{ans} = {anscnt}')
#Сумма последовательности
# seq = list(map(int, input().split()))
# seqsum = 0
# for i in range(len(seq)):
#     seqsum += seq[i]
# print(seqsum)
#Максимум последовательность
# seq = list(map(int, input().split()))
# if len(seq) == 0:
#     print("-inf")
# else:
#     seqmax = seq[0]
#     for i in range(1, len(seq)):
#         if seq[i] > seqmax:
#             seqmax = seq[i]
#     print(seqmax)
#Решение квадратного уравнение. Вывод корней в порядке возрастания
# a, b, c = map(int, input().split())
# if a == 0:
#     if b != 0:
#         print(-c / b)
#     if b == 0 and c == 0:
#         print("Infinity number of solutions")
# else:
#     d = b ** 2 - 4 * a * c
#     if d == 0:
#         x1 = -b / (2 * a)
#     elif d > 0:
#         x1 = (-b - m.sqrt(d)) / (2 * a)
#         x2 = (-b + m.sqrt(d)) / (2 * a)
#         if x1 < x2:
#             print(x2, x1)
#         else:
#             print(x1, x2)