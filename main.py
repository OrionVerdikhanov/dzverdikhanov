import os

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    contacts = []
    for line in lines:
        parts = line.strip().split(', ')
        if len(parts) == 4:
            contacts.append({'Фамилия': parts[0], 'Имя': parts[1], 'Отчество': parts[2], 'Номер телефона': parts[3]})
    return contacts

def save_data(filename, contacts):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(f"{contact['Фамилия']}, {contact['Имя']}, {contact['Отчество']}, {contact['Номер телефона']}\n")

def add_contact(contacts):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contacts.append({'Фамилия': surname, 'Имя': name, 'Отчество': patronymic, 'Номер телефона': phone_number})

def search_contacts(contacts):
    search_query = input("Введите фамилию, имя, отчество или номер телефона для поиска: ")
    found_contacts = [contact for contact in contacts if search_query in contact.values()]
    if found_contacts:
        for contact in found_contacts:
            print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']} - {contact['Номер телефона']}")
    else:
        print("Запись не найдена.")

def display_contacts(contacts):
    for contact in contacts:
        print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']} - {contact['Номер телефона']}")

def edit_contact(contacts):
    search_query = input("Введите фамилию контакта для редактирования: ")
    for i, contact in enumerate(contacts):
        if contact['Фамилия'] == search_query:
            print(f"Редактирование контакта: {contact['Фамилия']} {contact['Имя']} {contact['Отчество']} - {contact['Номер телефона']}")
            contacts[i] = {
                'Фамилия': input("Введите новую фамилию: "),
                'Имя': input("Введите новое имя: "),
                'Отчество': input("Введите новое отчество: "),
                'Номер телефона': input("Введите новый номер телефона: ")
            }
            print("Контакт обновлен.")
            return
    print("Контакт не найден.")

def main():
    filename = "contacts.txt"
    contacts = load_data(filename)

    while True:
        print("\n1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Найти контакт")
        print("4. Редактировать контакт")
        print("5. Сохранить и выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            edit_contact(contacts)
        elif choice == '5':
            save_data(filename, contacts)
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
