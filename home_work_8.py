import json
import csv

data = [
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": True,
        "languages": ["C++", "Python"]
    },
    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": False,
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": True,
        "languages": ["C#", "C++", "C"]
    }
]


with open('people.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


print("Файл people.json создан!")




def read_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return []



def json_to_csv():
    json_data = read_json('people.json')
    if not json_data:
        print("Нет данных для сохранения!")
        return


    all_fields = json_data[0].keys()


    with open('people.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=all_fields)
        writer.writeheader()
        for person in json_data:
            person_copy = person.copy()
            person_copy['languages'] = ', '.join(person['languages'])
            writer.writerow(person_copy)

    print("Данные сохранены в people.csv")



def add_to_json():
    print("\nДобавление нового сотрудника в JSON:")
    name = input("Имя: ")
    birthday = input("День рождения (дд.мм.гггг): ")
    height = int(input("Рост (см): "))
    weight = float(input("Вес (кг): "))
    car = input("Есть машина? (да/нет): ").lower() == 'да'

    print("Введите языки программирования через запятую:")
    languages = [lang.strip() for lang in input().split(',')]

    new_person = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages
    }


    json_data = read_json('people.json')
    json_data.append(new_person)


    with open('people.json', 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)

    print("Сотрудник добавлен в JSON файл!")



def add_to_csv():
    print("\nДобавление нового сотрудника в CSV:")
    name = input("Имя: ")
    birthday = input("День рождения (дд.мм.гггг): ")
    height = int(input("Рост (см): "))
    weight = float(input("Вес (кг): "))
    car = input("Есть машина? (да/нет): ").lower() == 'да'

    print("Введите языки программирования через запятую:")
    languages = [lang.strip() for lang in input().split(',')]

    new_person = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": ', '.join(languages)
    }

    with open('people.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=new_person.keys())
        writer.writerow(new_person)

    print("Сотрудник добавлен в CSV файл!")



def find_by_name():
    search_name = input("Введите имя для поиска: ")
    json_data = read_json('people.json')

    found = False
    for person in json_data:
        if search_name.lower() in person['name'].lower():
            print(f"\nНайден сотрудник: {person['name']}")
            print(f"День рождения: {person['birthday']}")
            print(f"Рост: {person['height']} см")
            print(f"Вес: {person['weight']} кг")
            print(f"Машина: {'Есть' if person['car'] else 'Нет'}")
            print(f"Языки: {', '.join(person['languages'])}")
            found = True

    if not found:
        print("Сотрудник не найден!")



def filter_by_language():
    language = input("Введите язык программирования: ")
    json_data = read_json('people.json')

    found = False
    print(f"\nСотрудники, владеющие {language}:")
    for person in json_data:
        if language in person['languages']:
            print(f"- {person['name']}")
            found = True

    if not found:
        print("Таких сотрудников нет!")



def filter_by_year():
    try:
        year = int(input("Введите год рождения: "))
        json_data = read_json('people.json')

        total_height = 0
        count = 0

        for person in json_data:
            birth_year = int(person['birthday'].split('.')[2])
            if birth_year < year:
                total_height += person['height']
                count += 1

        if count > 0:
            average = total_height / count
            print(f"Средний рост сотрудников, родившихся до {year} года: {average:.1f} см")
        else:
            print("Нет сотрудников, родившихся до этого года!")

    except ValueError:
        print("Ошибка! Введите корректный год.")



def main():
    while True:
        print("\n" + "=" * 50)
        print("МЕНЮ УПРАВЛЕНИЯ СОТРУДНИКАМИ")
        print("=" * 50)
        print("1. Преобразовать JSON в CSV")
        print("2. Добавить сотрудника в JSON")
        print("3. Добавить сотрудника в CSV")
        print("4. Найти сотрудника по имени")
        print("5. Фильтр по языку программирования")
        print("6. Фильтр по году рождения")
        print("7. Выйти из программы")
        print("=" * 50)

        choice = input("Выберите действие (1-7): ")

        if choice == '1':
            json_to_csv()
        elif choice == '2':
            add_to_json()
        elif choice == '3':
            add_to_csv()
        elif choice == '4':
            find_by_name()
        elif choice == '5':
            filter_by_language()
        elif choice == '6':
            filter_by_year()
        elif choice == '7':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")




main()