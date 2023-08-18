import pandas as pd

# Функция для вывода постранично записей из справочника на экран
def display_contacts(page_size, page_number):
    contacts = pd.read_csv('contacts.csv', encoding='cp1251')
    total_pages = len(contacts) // page_size + 1

    if page_number < 1 or page_number > total_pages:
        print("Недопустимый номер страницы.")
        return

    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    for _, contact in contacts.iloc[start_index:end_index].iterrows():
        print(contact)

# Функция для добавления новой записи в справочник
def add_contact():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    company = input("Введите название организации: ")
    personal_number = input("Введите личный телефон: ")
    work_number = input("Введите рабочий телефон: ")

    new_contact = pd.DataFrame({
        'Name': [name],
        'Surname': [surname],
        'Company': [company],
        'Personal_number': [personal_number],
        'Work_number': [work_number]
    })

    contacts = pd.read_csv('contacts.csv', encoding='cp1251')
    updated_contacts = pd.concat([contacts, new_contact], ignore_index=True)

    updated_contacts.to_csv('contacts.csv', index=False)
    print("Запись успешно добавлена.")


# Функция для редактирования записей в справочнике
def edit_contact():
    contact_id = input("Введите ID записи, которую хотите отредактировать: ")

    contacts = pd.read_csv('contacts.csv', encoding='cp1251')

    if int(contact_id) < 1 or int(contact_id) > len(contacts):
        print("Недопустимый ID записи.")
        return

    contact_index = int(contact_id) - 1
    contact = contacts.loc[contact_index]

    print("Текущая информация:")
    print(contact)

    name = input("Введите новое имя: ")
    surname = input("Введите новую фамилию: ")
    company = input("Введите новое название организации: ")
    personal_number = input("Введите новый личный телефон: ")
    work_number = input("Введите новый рабочий телефон: ")

    contacts.loc[contact_index, 'Name'] = name
    contacts.loc[contact_index, 'Surname'] = surname
    contacts.loc[contact_index, 'Company'] = company
    contacts.loc[contact_index, 'Personal_number'] = personal_number
    contacts.loc[contact_index, 'Work_number'] = work_number

    contacts.to_csv('contacts.csv', index=False)
    print("Запись успешно отредактирована.")

# Функция для поиска записей по одной или нескольким характеристикам
def search_contacts():
    search_criteria = input("Введите критерии поиска (через запятую): ")
    search_terms = [term.strip().lower() for term in search_criteria.split(',')]

    contacts = pd.read_csv('contacts.csv', encoding='cp1251')

    matching_contacts = contacts[
        contacts.apply(lambda row: all(term in row.astype(str).str.lower().values for term in search_terms), axis=1)
    ]

    if len(matching_contacts) == 0:
        print("Нет совпадающих записей.")
    else:
        print(matching_contacts)



# Основной код программы
while True:
    print("Телефонный справочник")
    print("1. Вывод записей")
    print("2. Добавление записи")
    print("3. Редактирование записи")
    print("4. Поиск записей")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        page_size = int(input("Введите размер страницы: "))
        page_number = int(input("Введите номер страницы: "))
        display_contacts(page_size, page_number)
    elif choice == '2':
        add_contact()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        search_contacts()
    elif choice == '5':
        break
    else:
        print("Недопустимый выбор. Попробуйте еще раз.")
