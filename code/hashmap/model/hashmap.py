
class Hashmap(object):

    def __get_hash(self, key):
        return hash(key) % self.__size

    def __init__(self, size=113):
        self.__size = size
        self.__obj = [None for _ in range(size)]
        pass

    def insert(self, key, value):
        h = self.__get_hash(key)
        self.__obj[h] = (key, value)

    def get(self, key):
        h = self.__get_hash(key)
        return self.__obj[h][1]

    def delete(self, key):
        h = self.__get_hash(key)
        if self.__obj[h] is None or self.__obj[h][0] != key:
            raise KeyError("No key {} in hashmap".format(key))
        else:
            self.__obj[h] = None
