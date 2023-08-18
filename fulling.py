import csv
import random
import string
import pandas as pd

#Заполнение датосета
# Генерация случайного имени
def generate_random_name():
    names = ['Alex', 'Max', 'Danil', 'Ivan', 'Artem', 'Nikita', 'Dima', 'Micle', 'Egor', 'Andrew']
    return random.choice(names)

# Генерация случайной фамилии
def generate_random_surname():
    surnames = ['Ivanov', 'Smirnov', 'Kuznecow', 'Popow', 'Vasiliev', 'Petrow', 'Socoloc', 'Mihailov', 'Novikov', 'Fedarov']
    return random.choice(surnames)

# Генерация случайной компании
def generate_random_company():
    companies = ['Apple Inc.', 'Google LLC', 'Microsoft Corporation', 'Amazon.com, Inc.', 'Facebook, Inc.', 'Tesla, Inc.', 'Samsung Electronics Co., Ltd.', 'Toyota Motor Corporation', 'Coca-Cola Company', 'Nike, Inc.']
    return random.choice(companies)

# Генерация случайного номера
def generate_random_number():
    return ''.join(random.choice(string.digits) for _ in range(10))

# Генерация случайного номера компании
def generate_random_company_number():
    return ''.join(random.choice(string.digits) for _ in range(10))


# Количество контактов для генерации
num_contacts = 100

# Открытие CSV файла для записи
with open('contacts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Surname', 'Company', 'Personal_number', 'Work_number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Заполнение CSV файла данными
    for _ in range(num_contacts):
        writer.writerow({
            'Name': generate_random_name(),
            'Surname': generate_random_surname(),
            'Company': generate_random_company(),
            'Personal_number': generate_random_number(),
            'Work_number': generate_random_company_number()
        })

print("CSV файл успешно заполнен!")

