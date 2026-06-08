import json
from json import JSONDecodeError

while True:
    try:
        with open("data/notes.json", 'r', encoding='utf-8') as notes_json:
            past_notes = json.load(notes_json)
    except FileNotFoundError:
        past_notes = []
    except json.JSONDecodeError:
        print("\nФайл notes.json поврежден, дальнейшее выполнение программы не возможно\n")
        break


    try:
        user_consent = int(input("1.Вывести все заметки\n"
                             "2.Добавить заметку\n"
                             "0.Выход\n"
                             "Выберете вариант:"))
        if user_consent == 1:
            for number, note in enumerate(past_notes, start=1):
                if number == 1:
                    print(f"\n{number}: {note}")
                elif number == len(past_notes):
                    print(f"{number}: {note}\n")
                else:
                    print(f"{number}: {note}")
        elif user_consent == 2:
            with open("data/notes.json", 'w', encoding='utf-8') as notes_json:
                past_notes.append(input("\nВведите новую заметку:"))
                json.dump(past_notes, notes_json, indent=4, ensure_ascii=False)
            print("\nЗаметка успешно добавлена\n")
        elif user_consent == 0:
            break
    except FileNotFoundError:
        print("\nФайл не найден, попробуйте для начала добавить заметку\n")
    except json.JSONDecodeError:
        print("\nФайл notes.json поврежден, дальнейшее выполнение программы не возможно\n")
    except ValueError:
        print("\nОшибка выбора\n")


