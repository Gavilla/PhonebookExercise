import pickle

phone_book_filename = ''

def load():
    with open(phone_book_filename, 'rb') as f:
        return pickle.load(f)

def save(obj):
    with open(phone_book_filename, 'wb') as f:
        pickle.dump(obj, f)