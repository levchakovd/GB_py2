# Задача 2: Найдите сумму цифр трехзначного числа.
num = int(input("введите трехзначное число: "))

while (99 > num < 1000):
    num = int(input("попробуем еще раз, ТРЕХЗНАЧНОЕ число: "))

sum = 0

while num > 0:
    sum += num % 10
    num = num // 10
print(sum)

#sum = sum(int(i) for i in str(num))
#print(sum)