import manage_record
import configurator

phone_book_name = ""
phone_book = {}
save = None
load = None

def request_name():
    return input("Please enter contact name\n")

def request_number():
    return input("Please enter contact number\n")

def request_create():
    name = request_name()
    number = request_number()
    manage_record.create_record(name, number)
    print(f"Contact '{name}' with number - {number} was added!\n")

def request_read():
    name = request_name()
    number = manage_record.read_record(name)
    print(f"'{name}' number is {number}!\n")

def request_update():
    name = request_name()
    number = request_number()
    manage_record.update_record(name, number)
    print(f"'{name}' new number is {number}!\n")

def request_delete():
    name = request_name()
    manage_record.delete_record(name)
    print(f"Contact '{name}' was deleted!\n")

def request_exit():
    save_phone_book()
    exit()

actions = {
    '1': {'name': 'Create contact', 'action': request_create},
    '2': {'name': 'Find contact', 'action': request_read},
    '3': {'name': 'Update contact', 'action': request_update},
    '4': {'name': 'Delete contact', 'action': request_delete},
    'q': {'name': 'Exit', 'action': request_exit},
}

def request_input():
    print("Please choose an action (enter number of desired action):")
    for action_code, action in actions.items():
        print(f"{action_code}. {action['name']}")
    return input()

def request_new_input():
    print("Incorrect input. Please enter a number 1-4 to choose desired action!\n")

def load_phone_book():
    try:
        phone_book = load()
    except Exception as e:
        print(f'Exception occured while reading phone_book data!\n{e}!')
        print('No phone_book was loaded!')
        phone_book = {}
    return phone_book

def save_phone_book():
    global phone_book
    try:
        save(manage_record.phone_book)
    except Exception as e:
        print(f'Exception occured while saving phone_book data!\n{e}!')
        print('No data was saved!')


def run():
        global phone_book, save, load
        try:
           save, load = configurator.read()
        except Exception as e:
            print(f'Exception occured while config file!\n{e}!')

        manage_record.phone_book = load_phone_book()

        while True:
            action = request_input()
            action_func = actions.get(action, {}).get('action', request_new_input)
            try:
                action_func()
            except KeyError as e:
                print(e)