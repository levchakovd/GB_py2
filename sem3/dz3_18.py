# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

x = int(input("Вводим Х: "))
n = int(input("Вводим кол-во элементов массива: "))
A = []

for i in range(1, n+1):
    A.append(i)

print(A)

if x in A:
    print(f"самое близкое к числу {x} в списке, является число {x}")
elif x > A[n-1]:
    print(f"самое близкое к числу {x} в списке, является число {A[n-1]}")
else:
    print(f"самое близкое к числу {x} в списке, является число {A[0]}")