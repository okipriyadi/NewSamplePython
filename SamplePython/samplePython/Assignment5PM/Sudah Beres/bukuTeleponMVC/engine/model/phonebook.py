import os.path
import json

class PhonebookModel:
    filepath = 'files/phonebook.json'

    def __init__(self):
        if not self.__fileexists():
            self.__initfile()

    def __fileexists(self):
        return os.path.exists(self.filepath)

    def __initfile(self):
        tmp = open(self.filepath, 'w+')
        tmp.close()

    def read(self):
        fn = open(self.filepath, 'r+')
        string = fn.read()
        fn.close()
        return string

    def write(self, string):
        fn = open(self.filepath, 'w+')
        fn.write(string)
        fn.close()

    def readjson(self):
        string = self.read()
        if string!='':
            return json.loads(string)
        else:
            return []

    def writejson(self, obj):
        self.write(json.dumps(obj))
    
    