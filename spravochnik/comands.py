import easygui
import json

DATA_FILE = 'baza.json'
    
# Загрузка данных из файла
try:
    with open(DATA_FILE, 'r') as f:
        phonebook = json.load(f)
except FileNotFoundError:
    # Если файл не найден, создаем пустой словарь
    phonebook = {}


def load_phonebook():
    with open(DATA_FILE, 'r') as f:
        phonebook = json.load(f)
        return phonebook


def save_phonebook(phonebook):
    with open(DATA_FILE, "w") as f:
        json.dump(phonebook, f)

def search_contact():
    name = easygui.enterbox("Введите имя контакта:")
    phonebook = load_phonebook()
    if name in phonebook:
        contact = phonebook[name]
        message = f"Контакт: {name}\n"
        for key, value in contact.items():
            message += f"{key}: {value}\n"
        easygui.msgbox(message)
    else:
        easygui.msgbox(f"Контакт {name} не найден.")

def show_contacts():
    phonebook = load_phonebook()
    if phonebook:
        message = ""
        for name, contact in phonebook.items():
            message += f"Контакт: {name}\n"
            for key, value in contact.items():
                message += f"{key}: {value}\n"
            message += "\n"
        easygui.msgbox(message)
    else:
        easygui.msgbox("Справочник пустой.")
        
def add_contact():
    values = easygui.multenterbox("Введите данные контакта", fields=["Имя", "Фамилия", "Отчество", "Телефон"])
    while True:
        if values is None:
            break
        elif "" in values:
            easygui.msgbox("Необходимо заполнить все поля.")
            values = easygui.multenterbox("Введите данные контакта", fields=["Имя", "Фамилия", "Отчество", "Телефон"])
        else:
            break
        
    if values is not None:
        name = f"{values[0]} {values[1]} {values[2]}"
        phonebook[name] = {"Имя": values[0], "Фамилия": values[1], "Отчество": values[2], "Телефон": values[3]}
        save_phonebook(phonebook)
        easygui.msgbox(f"Контакт {name} успешно добавлен.")


def delete_contact():
    # Проверяем, есть ли контакты в телефонной книге
    if not phonebook:
        easygui.msgbox("Телефонная книга пуста!")
        return
    # Создаем список имен контактов
    choices = list(phonebook.keys())
    
    # Отображаем диалоговое окно для выбора контакта для удаления
    choice = easygui.choicebox("Выберите контакт для удаления:", "Удаление контакта", choices)
    
    # Если выбрано "Отмена", выходим из функции
    if not choice:
        return
    
    # Переспрашиваем, уверены ли мы, что хотим удалить контакт
    msg = f"Вы действительно хотите удалить контакт '{choice}'?"
    title = "Удаление контакта"
    if not easygui.ynbox(msg, title, ("Да", "Нет")):
        return

    # Удаляем контакт из телефонной книги
    del phonebook[choice]
    with open("phonebook.json", "w") as f:
        json.dump(phonebook, f)


    # Сообщаем пользователю, что контакт успешно удален
    easygui.msgbox(f"Контакт '{choice}' успешно удален!")


def redact_contacts():
    return