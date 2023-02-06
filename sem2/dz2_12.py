#Петя и Катя – брат и сестра. Петя – студент, а Катя –
#школьница. Петя помогает Кате по математике. Он задумывает два
#натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
#этого Петя делает две подсказки. Он называет сумму этих чисел S и их
#произведение P. Помогите Кате отгадать задуманные Петей числа.
import math

S = int(input("Введи сумму чисел(подсказка 1): "))
P = int(input("Введи произведение чисел(подсказка 2): "))

if (S**2 - 4*P) < 0:
    X = None
    Y = None
else:
    X = int((S + math.sqrt(S**2 - 4*P)) / 2)
    Y = int((S - math.sqrt(S**2 - 4*P)) / 2)

print(f"X: {X}, Y: {Y}")