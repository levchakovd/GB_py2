#Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) . 
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, 
# сами значения предикатов случайные, проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , 
# сколько времени отработала программа. В конце вывести результат проверки истинности этого утверждения.

import random
import time

predicates = int(input(": "))

def de_morgan(predicates):
    result = True
    for i in range(100):
        predicates = [random.choice([True, False]) for i in range(5, 26)]
        X_or_Y_or_Z = random.choice([True, False])
        for x in predicates:
            X_or_Y_or_Z |= x
        not_X_or_Y_or_Z = not X_or_Y_or_Z
        not_X_and_not_Y_and_not_Z = True
        for x in predicates:
            not_X_and_not_Y_and_not_Z &= not x
        result &= (not_X_or_Y_or_Z == not_X_and_not_Y_and_not_Z)
    return result

start = time.time()
result = de_morgan(predicates)
end = time.time()

print("Time elapsed:", end - start, "seconds")
print("The statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is", result)
