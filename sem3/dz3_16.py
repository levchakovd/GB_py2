# : Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

x = int(input("Вводим Х: "))
n = int(input("Вводим кол-во элементов массива: "))
A = []

for i in range(1, n+1):
    A.append(i)

# if x in A:
#     print(x," встречается один раз")
# else:
#     print(x," в списке не встречается")
# поскольку это список последовательных натуральных чисел, подошел бы и такой вариант решения, но можно и посчитать
count = 0
for y in range(n):
    if A[y] == x:
        count +=1
print(A)
print(f"X: {x}, встречается в списте: {count} раз")