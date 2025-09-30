import json
phone_book_filename = ''

def load():
    with open(phone_book_filename, 'rt') as f:
        return json.load(f)

def save(obj):
    with open(phone_book_filename, 'wt') as f:
        json.dump(obj, f)