#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#*Пример:*
#
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] !!! задание с ошибкой

def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def negofibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


k = int(input("k = "))
fibo = [0]
for i in range(1, k+1):
    fibo.append(fibonacci(i))
    fibo.insert(0,negofibonacci(i))

print(fibo)










