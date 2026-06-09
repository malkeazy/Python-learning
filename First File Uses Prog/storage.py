import json

def return_past_notes(storage_file: str):
    try:
        with open(storage_file, 'r', encoding='utf-8') as notes_json:
            past_notes = json.load(notes_json)
        return past_notes
    except FileNotFoundError:
        past_notes = []
        return past_notes
    except json.JSONDecodeError:
        return None

def add_note(storage_file: str, new_note: str):
    past_notes = return_past_notes(storage_file)
    with open(storage_file, 'w', encoding='utf-8') as notes_json:
        past_notes.append(new_note)
        json.dump(past_notes, notes_json, indent=4, ensure_ascii=False)
    print("\nЗаметка успешно добавлена\n")

def delete_note(storage_file: str, number_int: int):
    past_notes = return_past_notes(storage_file)
    if number_int > 0:
        del past_notes[number_int - 1]
    else:
        print("Заметка не удалена, введен неверный номер1")
        return None

    try:
        with open(storage_file, 'w', encoding='utf-8') as notes_json:
            json.dump(past_notes, notes_json, indent=4, ensure_ascii=False)
        print("\nЗаметка успешно удалена\n")
    except FileNotFoundError:
        print("\nФайл не найден, попробуйте для начала добавить заметку\n")
        return None