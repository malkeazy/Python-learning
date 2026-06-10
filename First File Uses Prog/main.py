import storage, json

while True:
    file_locate = "data/notes.json"
    past_notes = storage.return_past_notes(file_locate)

    try:
        user_consent = int(input("\n1.Вывести все заметки\n"
                             "2.Добавить заметку\n"
                             "3.Удалить заметку\n"
                             "0.Выход\n"
                             "Выберете вариант:"))
        if user_consent == 1:
            if len(past_notes) > 0:
                for number, note in enumerate(past_notes, start=1):
                    if number == 1:
                        print(f"\n{number}: {note}")
                    else:
                        print(f"{number}: {note}")
            else:
                print("\nФайл еще не имеет заметок создайте пожалуйста")
        elif user_consent == 2:
            status_add_note = storage.add_note(file_locate, input("\nВведите новую заметку:"))
            if status_add_note:
                print("\nЗаметка успешно добавлен")
            else:
                print("\nЗаметка не добавлен")
        elif user_consent == 3:
            if len(past_notes) > 0:
                number_note = int(input("\nВведите номер заметки:"))
                if number_note > 0:
                    storage.delete_note(file_locate, number_note)
                    print("\nЗаметка успешно удалена")
                else:
                    print("\nЗаметка не удалена, введен неверный номер")
                    continue
            else:
                print("\nВ файле еще не сущевствует ни одной заметки")
        elif user_consent == 0:
            break
    except json.JSONDecodeError:
        print("\nОшибка, файл поврежден")
    except ValueError:
        print("\nОшибка выбора")
    except IndexError:
        print("\nВведен неверный индекс")


