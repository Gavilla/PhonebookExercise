import json
from . import *

class SerJson(Serializer):
    def __init__(self, file_name = ''):
        super().__init__(file_name) 

    def load(self):
        with open(self.filename , 'rt') as f:
            return json.load(f)

    def save(self,obj):
        with open(self.filename , 'wt') as f:
            json.dump(obj, f)