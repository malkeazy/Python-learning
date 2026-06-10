import storage, json, os

while True:
    file_locate = "data/notes.json"
    try:
        past_notes = storage.return_past_notes(file_locate)
    except json.JSONDecodeError:
        choose = (input("\nФайл повреджден\n"
                             "1.Удалить файл и создать заново\n"
                             "0.Выход из программы\n"
                             "Выберете вариант:"))
        if choose == "1":
            try:
                os.remove(file_locate)
                print("Файл успешно удален")
            except FileNotFoundError:
                print("Файл уже отсутствует")
            except PermissionError:
                print("Недостаточно прав для удаления файла")
            past_notes = []
            continue
        elif choose == "0":
            break
        else:
            print("Неверный выбор")
            continue
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
            storage.add_note(file_locate, input("\nВведите новую заметку:"), past_notes)
            print("\nЗаметка успешно добавлен")
        elif user_consent == 3:
            if len(past_notes) > 0:
                number_note = int(input("\nВведите номер заметки:"))
                if number_note > 0:
                    storage.delete_note(file_locate, number_note, past_notes)
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


