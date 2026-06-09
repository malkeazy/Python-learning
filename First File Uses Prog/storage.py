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

def add_note(storage_file: str, new_note: str) -> str:
    past_notes = return_past_notes(storage_file)
    with open(storage_file, 'w', encoding='utf-8') as notes_json:
        past_notes.append(new_note)
        json.dump(past_notes, notes_json, indent=4, ensure_ascii=False)
    return "\nЗаметка успешно добавлена\n"

def delete_note(storage_file: str, number_str: int):
    past_notes = return_past_notes(storage_file)
    with open(storage_file, 'w', encoding='utf-8') as notes_json:
        past_notes.remove(number_str-1)
        json.dump(past_notes, notes_json, indent=4, ensure_ascii=False)
    print("\nЗаметка успешно удалена\n")