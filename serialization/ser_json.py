import json
phone_book_filename = ''

def load():
    with open(phone_book_filename, 'rb') as f:
        return json.load(f)

def save(obj):
    with open(phone_book_filename, 'wb') as f:
        json.dump(obj, f)