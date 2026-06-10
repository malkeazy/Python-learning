import json

def return_past_notes(storage_file: str) -> list:
    try:
        with open(storage_file, 'r', encoding='utf-8') as notes_json:
            past_notes = json.load(notes_json)
        return past_notes
    except FileNotFoundError:
        past_notes = []
        return past_notes

def add_note(storage_file: str, new_note: str, past_notes: list):
    with open(storage_file, 'w', encoding='utf-8') as notes_json:
        past_notes.append(new_note)
        json.dump(past_notes, notes_json, indent=4, ensure_ascii=False)

def delete_note(storage_file: str, number_int: int, past_notes: list):
    del past_notes[number_int - 1]
    with open(storage_file, 'w', encoding='utf-8') as notes_json:
        json.dump(past_notes, notes_json, indent=4, ensure_ascii=False)