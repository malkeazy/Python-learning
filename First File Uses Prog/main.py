import json
while True:
    try:
        user_consent = int(input("1.Вывести все заметки\n"
                             "2.Добавить заметку\n"
                             "0.Выход\n"
                             "Выберете вариант:"))
        if user_consent == 1:
            with open("data/notes.json", 'r', encoding='utf-8') as notes_json:
                notes = json.load(notes_json)
            print(notes)
        elif user_consent == 2:
            with open("data/notes.json", 'w', encoding='utf-8') as notes_json:
                json.dump(input("Введите новую заметку:"), notes_json, indent=4, ensure_ascii=False)
            print("Заметка успешно добавлена")
        elif user_consent == 0:
            break
    except FileNotFoundError:
        print("Файл не найден, попробуйте для начала добавить заметку")
    except ValueError:
        print("Ошибка выбора")

