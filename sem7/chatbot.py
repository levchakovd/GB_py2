from random import *
import json

teams = []
teams.append("Кливленд")
teams.append("Лейкерс")
teams.append("Портленд")
teams.append("Атланта")
teams.append("Денвер")

def save():
    with open("teams.json","w",encoding="utf-8") as tm:
        tm.write(json.dumps(teams,ensure_ascii=False))
    print("Мы добавили команду в список")

while True:
    command = input("введите команду боту: ")
    if command == "/start":
        print("БОТ NBA начал свою работу")
    elif command == "/stop":
        print("я перестал работать, увидимся")
        break
    elif command == "/all":
        print("Вот список команд")
        print(teams)
    elif command == "/add":
        t = input("Введите название команды: ")
        teams.append(t)
    elif command == "/delete":
        d = input("Введите название команды, которуе нужно удалить")
    elif command == "/save":
        save()
    else:
        print("я хз что тебе надо, не умею это")
