'''insert auto doc - phonebook controller'''
class Phonebook:
    def __init__ (self, cont = None):
        if cont is None: self.contacts = {}
        else: self.contacts = cont


    def to_dict(self):
        dict_cont = {}
        for contact in self.contacts:
            dict_cont[contact] = self.contacts[contact]
        return dict_cont

    @staticmethod
    def verify_contact(is_contact, get_error_msg):
        def decorator(func):
            def wrapper(self,contact, *args):
                if (contact in self.contacts) == is_contact:
                    return func(self, contact, *args)
                else:
                    raise KeyError(get_error_msg(contact, *args))
            return wrapper
        return decorator

    verify_true = verify_contact(True, lambda contact,*args: f"Contact '{contact}' doesn't exist!")
    verify_false = verify_contact(False, lambda contact,*args: f"Contact '{contact}' already exist!")

    @verify_false
    def create_contact(self,contact, value, address = "", email = ""):
        self.contacts[contact.lower()] = ContactDetails(value,address,email)

    @verify_true
    def read_contact(self, contact):
        return self.contacts[contact.lower()]

    @verify_true
    def update_contact(self,contact, value, address = "", email = ""):
        self.contacts[contact.lower()] = ContactDetails(value,address,email)

    @verify_true
    def delete_contact(self,contact):
        del self.contacts[contact.lower()]

class ContactDetails:
    def __init__(self, v, a, e):
        self.number = v
        self.address = a
        self.email = e