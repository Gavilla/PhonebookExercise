'''insert auto doc - phonebook controller'''

phone_book = {}

def verify_record(is_record, get_error_msg):
    def decorator(func):
        def wrapper(record, *args):
            if (record in phone_book) == is_record:
                return func(record, *args)
            else:
                raise KeyError(get_error_msg(record, *args))
        return wrapper
    return decorator

verify_true = verify_record(True, lambda record,*args: f"Record '{record}' doesn't exist!")
verify_false = verify_record(False, lambda record,*args: f"Record '{record}' already exist!")

@verify_false
def create_record(record, value):
    phone_book[record] = value

@verify_true
def read_record(record):
    return phone_book[record]

@verify_true
def update_record(record, value):
    phone_book[record] = value

@verify_true
def delete_record(record):
    del phone_book[record]