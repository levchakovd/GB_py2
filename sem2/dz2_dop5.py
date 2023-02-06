#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в N-мерном пространстве. 
# Сначала задается N с клавиатуры, потом задаются координаты точек.

import math

def distance(point1, point2, N):
    sum = 0
    for i in range(N):
        sum += (point2[i] - point1[i])**2
    return math.sqrt(sum)

N = int(input("Введите размер пространства: "))
point1 = []
point2 = []

for i in range(N):
    x = int(input("Введите координаты первой точки в измерении " + str(i + 1) + ": "))
    point1.append(x)

for i in range(N):
    y = int(input("Введите координаты второй точки в измерении " + str(i + 1) + ": "))
    point2.append(y)

print("Расстояние между двумя точками равно: ", distance(point1, point2, N))


