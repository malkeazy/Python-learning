try:
    notes_txt = open("data/notes.txt", 'r', encoding='utf-8')
    notes = notes_txt.read()
    if len(notes) > 0:
        print(notes)
    while True:
        user_consent = input("Хотите ли добавить заметку Y-yes N-no:")
        if user_consent.upper() == "Y":
            with open("data/notes.txt", 'a', encoding='utf-8') as notes_txt:
                notes_txt.write(input("Введите новую заметку:") + "\n")
            print("Заметка успешно добавлена")
            break
        elif user_consent.upper() == "N":
            print("Файл остался без изменений")
            break
except FileNotFoundError:
    print("Файл не найден")

