import json, storage

while True:
    file_locate = "data/notes.json"
    past_notes = storage.return_past_notes(file_locate)
    if past_notes is None:
        print("файл поврежден")
        break

    try:
        user_consent = int(input("1.Вывести все заметки\n"
                             "2.Добавить заметку\n"
                             "3.Удалить заметку\n"
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
            storage.add_note(file_locate, input("\nВведите новую заметку:"))
        elif user_consent == 3:
            storage.delete_note(file_locate, int(input("\nВведите номер заметки:")))
        elif user_consent == 0:
            break
    except FileNotFoundError:
        print("\nФайл не найден, попробуйте для начала добавить заметку\n")
    except ValueError:
        print("\nОшибка выбора\n")
    except IndexError:
        print("\nВведен неверный индекс\n")


