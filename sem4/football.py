# Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Sample Input: 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

n = int(input('количество игр: '))
x_list = [input('команда1;кол-во голов;комана2;кол-во голов: ').split(';') for x in range(n)]
vs = [(x[0], x[2]) for x in x_list]

import itertools

clubs = set(itertools.chain.from_iterable(vs))
res = {club:[0, 0, 0, 0, 0] for club in clubs}
for kom1, gol1, kom2, gol2 in x_list:
    res[kom1][0] += 1
    res[kom2][0] += 1
    if int(gol1) > int(gol2):
        res[kom1][1] += 1
        res[kom1][4] += 3
        res[kom2][3] += 1
    elif int(gol1) < int(gol2):
        res[kom2][1] += 1
        res[kom2][4] += 3
        res[kom1][3] += 1
    elif int(gol1) == int(gol2):
        res[kom1][2] += 1
        res[kom1][4] += 1
        res[kom2][2] += 1
        res[kom2][4] += 1
for club in clubs:
    print('{}:{}'.format(club, ' '.join(map(str, res[club]))))

