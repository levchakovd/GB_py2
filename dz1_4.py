# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#в чем задача заключается, объясните мне пожалуйста?
#Петя сделал S/6, Сережа S/6, Катя сделала 2S/3
#программирование и код в чем заключаются?

S = int(input("число S = "))

while (S%6 != 0):
    print("с этим числом ничего не выйдет, оно должно быть кратно 6, такая крутая задача")
    S = int(input("число S = "))

print("Петя и Сережа сделали по", int(S/6), "журавликов, а Катя ", int(2*S/3))