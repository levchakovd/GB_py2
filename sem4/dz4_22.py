# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from collections import Counter

n = int(input("кол-во эл-тов первого множества: "))
m = int(input("кол-во эл-тов второго множества: "))
N = [int(input("Введите число из первого множества: ")) for i in range(n)]
M = [int(input("Введите число из второго множества: ")) for i in range(m)]

def intersection(list1, list2):
    c1, c2 = Counter(list1), Counter(list2)
    common_elements = set(c1.keys()) & set(c2.keys())
    return sorted(list(common_elements))
print(N)
print(M)
print(intersection(N,M))