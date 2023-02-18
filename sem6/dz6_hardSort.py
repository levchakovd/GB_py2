# Задача HARD SORT необязательная.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10
import random
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Инициализируем двумерный массив 
matrix = [[random.randint(0,10) for j in range(cols)] for i in range(rows)]

# Выводим массив на экран
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()

print("-"*cols)
#объеденяем все в один список
flat_matrix = [num for row in matrix for num in row]

#сортируем полученный список
flat_matrix.sort()

#собираем мартицу отсортированную
sorted_matrix = [flat_matrix[i:i+cols] for i in range(0, len(flat_matrix), cols)]

# Выводим массив на экран
for i in range(rows):
    for j in range(cols):
        print(sorted_matrix[i][j], end=' ')
    print()