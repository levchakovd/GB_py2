from defs import *
import easygui

FILENAME = "baza4.json"
    
while True:
    # Загрузка данных из файла
    try:
        with open(FILENAME, 'r') as f:
            phonebook = json.load(f)
    except FileNotFoundError:
    # Если файл не найден, создаем пустой словарь
        phonebook = {}
    
    choice = easygui.buttonbox("Справочник", choices=["Добавить контакт", "Поиск", "Все контакты", "Удалить контакт", "Редактировать контакт", "Выход"])

    if choice == "Добавить контакт":
        add_contact()
    elif choice == "Поиск":
        search_contact()
    elif choice == "Все контакты":
        show_contacts()
    elif choice == "Удалить контакт":
        delete_contact()
    elif choice == "Редактировать контакт":
        redact_contact()
    elif choice == "Выход":
        break