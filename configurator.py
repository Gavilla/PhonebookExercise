from serialization import ser_pickle,ser_json
import os
import configparser

CONFIG_FILENAME = 'config.ini'

def read():
    config = configparser.ConfigParser()
    try:
        config.read(CONFIG_FILENAME)
    except Exception as e:
        print(f'Exception while reading config file!\n{e}')
    
    phone_book_filename = config.get('file', 'filename', fallback='')
    _, extention = os.path.splitext(phone_book_filename)
    print(f"filename: {phone_book_filename} - extention: {extention}")
    match extention:
        case '.pickle':
            ser_pickle.phone_book_filename = phone_book_filename
            save, load = ser_pickle.save, ser_pickle.load
        case '.json':
            ser_json.phone_book_filename = phone_book_filename
            save, load = ser_json.save, ser_json.load
        case _:
           raise ValueError(f"Exception while serializing the file!")

    return save, load