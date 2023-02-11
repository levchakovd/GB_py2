# задача калькулятор необязательная.
# Решать только через рекурсию!. Пользоваться встроенными функциями вычисления таких выражений нельзя, 
# если только для проверки вашего алгоритма.
# на вход подается строка из операторов / * + - и целых чисел. Надо посчитать результат введенного выражения.
# Например,

# на входе
# 1+9/3*7-4
# на выходе
# 18

def calc_expr(expr):
    # Определяем индекс первого оператора в выражении
    op_index = -1
    for i in range(len(expr)):
        if expr[i] in "+-":
            op_index = i
            break
    # Если оператор не найден, то это просто число
    if op_index == -1:
        return int(expr)
    # Разбиваем выражение на две части по индексу оператора
    left = expr[:op_index]
    right = expr[op_index + 1:]
    # Вычисляем левую и правую части рекурсивно
    left_result = calc_term(left)
    right_result = calc_expr(right)
    # Выполняем операцию между левой и правой частью
    if expr[op_index] == "+":
        return left_result + right_result
    else:
        return left_result - right_result

def calc_term(term):
    # Определяем индекс первого оператора в выражении
    op_index = -1
    for i in range(len(term)):
        if term[i] in "*/":
            op_index = i
            break
    # Если оператор не найден, то это просто число
    if op_index == -1:
        return int(term)
    # Разбиваем выражение на две части по индексу оператора
    left = term[:op_index]
    right = term[op_index + 1:]
    # Вычисляем левую и правую части рекурсивно
    left_result = calc_term(left)
    right_result = calc_term(right)
    # Выполняем операцию между левой и правой частью
    if term[i] == "*":
        return left_result*right_result
    else:
        return left_result/right_result

