# задача 2 HARD необязательная
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно и только один раз 
# переместился на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то 
# надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

import random
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
if n*m %2 != 0:
    while (n*m %2 != 0):
        print("так не получится, давайте сделаем так, чтобы кол-во эл-тов было четным!")
        m = int(input("Введите количество строк: "))
        n = int(input("Введите количество столбцов: "))


# Инициализируем двумерный массив 
matrix = [[random.randint(0,10) for j in range(m)] for i in range(n)]

# Выводим массив на экран
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

print("-"*m)

flat_matrix = [num for row in matrix for num in row]
#print(flat_matrix)

#выглядит как костыль, но:
randrange = list(range(0,len(flat_matrix)))
random.shuffle(randrange)
#print(randrange)

count = 0

for i in range(int(m*n/2)):
    flat_matrix[randrange[i]],flat_matrix[randrange[i+1]] = flat_matrix[randrange[i+1]],flat_matrix[randrange[i]]
    count +=1

print(f"количество иттераций = {count}")

result = []
for i in range(n):
    res = []
    for j in range(m):
        idx = i*m+j
        if idx < len(flat_matrix):
            res.append(flat_matrix[idx])
        else:
            res.append(None)
    result.append(res)

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()




