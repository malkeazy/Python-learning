try:
    while True:
        user_consent = input("1.Вывести все заметки\n"
                             "2.Добавить заметку\n"
                             "Выберете вариант:\n")
        if user_consent == "1":
            with open("data/notes.txt", 'r', encoding='utf-8') as notes_txt:
                notes = notes_txt.readline()
            if len(notes) > 0:
                print(notes)
            else:
                print("Файл пустой")
            break
        elif user_consent.upper() == "2":
            with open("data/notes.txt", 'a', encoding='utf-8') as notes_txt:
                notes_txt.write(input("Введите новую заметку:") + "\n")
            print("Заметка успешно добавлена")
            break
except FileNotFoundError:
    print("Файл не найден")

