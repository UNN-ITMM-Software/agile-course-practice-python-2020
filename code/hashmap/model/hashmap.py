
class Hashmap(object):

    def __init__(self):
        self.__obj = None
        pass

    def insert(self, key, value):
        self.__obj = value

    def get(self, key):
        return self.__obj

    def delete(self, key):
        pass
