while True:
    try:
        user_consent = int(input("1.Вывести все заметки\n"
                             "2.Добавить заметку\n"
                             "0.Выход\n"
                             "Выберете вариант:\n"))
        if user_consent == 1:
            with open("data/notes.txt", 'r', encoding='utf-8') as notes_txt:
                notes = notes_txt.read()
            if len(notes) > 0:
                print(notes)
            else:
                print("Файл пустой")
        elif user_consent == 2:
            with open("data/notes.txt", 'a', encoding='utf-8') as notes_txt:
                notes_txt.write(input("Введите новую заметку:") + "\n")
            print("Заметка успешно добавлена")
        elif user_consent == 0:
            break
    except FileNotFoundError:
        print("Файл не найден")
    except ValueError:
        print("Ошибка выбора")

