import pickle
from . import *

class SerPickle(Serializer):
    def __init__(self, file_name = ''):
        super().__init__(file_name) 

    def load(self):
        with open(self.filename, 'rb') as f:
            return pickle.load(f)

    def save(self,obj):
        with open(self.filename, 'wb') as f:
            pickle.dump(obj, f)