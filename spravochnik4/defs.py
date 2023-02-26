import easygui
import json
import os

FILENAME = os.path.join(os.path.dirname(__file__), 'baza4.json')

try:
    with open(FILENAME, 'r') as f:
        phonebook = json.load(f)
except FileNotFoundError:
    # Если файл не найден, создаем пустой словарь
    phonebook = {}


def load_phonebook():
    with open(FILENAME, 'r') as f:
        phonebook = json.load(f)
        return phonebook

def save_phonebook(phonebook):
    with open(FILENAME, 'w') as f:
        json.dump(phonebook,f)

def add_contact():
    values = easygui.multenterbox("Введите данные контакта", fields=["Фамилия", "Имя", "Отчество", "Телефон"])
    while True:
        if values is None:
            break
        elif "" in values:
            easygui.msgbox("Необходимо заполнить все поля.")
            values = easygui.multenterbox("Введите данные контакта", fields=["Фамилия", "Имя", "Отчество", "Телефон"])
        else:
            break
        
    if values is not None:
        name = f"{values[0]} {values[1]} {values[2]}"
        phonebook[name] = {"Фамилия": values[0], "Имя": values[1], "Отчество": values[2], "Телефон": values[3]}
        save_phonebook(phonebook)
        easygui.msgbox(f"Контакт {name} успешно добавлен.")


def search_contact():
    search = easygui.enterbox("Введите фамилию, имя, отчество или номер телефона контакта для поиска:")
    results = []
    for contact in phonebook.values():
        if search.lower() in contact["Фамилия"].lower() or search.lower() in contact["Имя"].lower() or search.lower() in contact["Отчество"].lower() or search in contact["Телефон"]:
            results.append(contact)
    if results:
        message = "Найденные контакты:\n"
        for contact in results:
            message += f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}\n"
        easygui.msgbox(message, title="Результаты поиска")
    else:
        easygui.msgbox("Контакты не найдены", title="Результаты поиска")



def show_contacts():
    # Проверяем, что в справочнике есть контакты
    if not phonebook:
        easygui.msgbox("Справочник пуст.")
        return
    # Создаем список всех контактов в справочнике
    choices = sorted(phonebook.keys())
    # Просим пользователя выбрать контакт чтобы показать его
    choice = easygui.choicebox("Выберите контакт:", "Показать номер телефона", choices)
    # Если пользователь нажал "Отмена", просто выходим из функции
    if choice is None:
        return
    # Получаем номер телефона для выбранного контакта
    phone_number = phonebook[choice]['Телефон']
    # Выводим номер телефона на экран
    easygui.msgbox(phone_number, title="Вот номер телефона")

                   
def delete_contact():
    # Проверяем, что в справочнике есть контакты
    if not phonebook:
        easygui.msgbox("Справочник пуст.")
        return
    
    # Создаем список всех контактов в справочнике
    choices = sorted(phonebook.keys())
    
    # Просим пользователя выбрать контакт для удаления
    choice = easygui.choicebox("Выберите контакт для удаления:", "Удаление контакта", choices)
    
    if choice:
        # Просим пользователя подтвердить удаление контакта
        msg = f"Вы уверены, что хотите удалить контакт {choice}?"
        confirm = easygui.buttonbox(msg, "Удаление контакта", choices=["Да, удаляй", "Нет, я передумал"])
        
        if confirm == "Да, удаляй":
            # Удаляем выбранный контакт из справочника
            del phonebook[choice]
            # Сохраняем изменения в файл
            with open(FILENAME, 'w') as f:
                json.dump(phonebook, f)
            easygui.msgbox(f"Контакт {choice} успешно удален.")


def redact_contact():
    global phonebook

    # Проверка, что список не пустой
    if not phonebook:
        easygui.msgbox("Список контактов пуст.")
        return

    # Получаем список контактов
    contacts = list(phonebook.keys())
    
    # Предлагаем пользователю выбрать контакт для редактирования
    chosen_contact = easygui.choicebox("Выберите контакт для редактирования:", choices=contacts)
    if chosen_contact is None:
        return

    # Предлагаем пользователю выбрать, какое значение нужно изменить
    choices = ["Фамилия", "Имя", "Отчество", "Телефон"]
    chosen_field = easygui.buttonbox("Выберите, какое значение нужно изменить:", choices=choices)

    # Получаем старое значение выбранного поля контакта
    old_value = phonebook[chosen_contact][chosen_field]

    # Запрашиваем новое значение для выбранного поля контакта
    new_value = easygui.enterbox(f"Введите новое значение для {chosen_field}:", default=old_value)
    if new_value is None:
        return

    # Обновляем значение поля контакта в словаре
    phonebook[chosen_contact][chosen_field] = new_value
    save_phonebook(phonebook)
    easygui.msgbox(f"Значение {chosen_field} для контакта {chosen_contact} успешно изменено с {old_value} на {new_value}.")

