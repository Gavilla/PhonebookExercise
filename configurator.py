from serialization import Serializer,ser_pickle,ser_json
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
    serializer = Serializer()
    match extention:
        case '.pickle':
            serializer = ser_pickle.SerPickle(phone_book_filename)
        case '.json':
            serializer = ser_json.SerJson(phone_book_filename)
        case _:
           raise ValueError(f"Exception while serializing the file!")

    return serializer