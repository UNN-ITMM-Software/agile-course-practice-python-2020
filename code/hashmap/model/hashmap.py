
class Hashmap(object):

    def __init__(self, size=113):
        self.__size = size
        self.__obj = [None for _ in range(size)]
        pass

    def insert(self, key, value):
        h = hash(key) % self.__size
        self.__obj[h] = (key, value)

    def get(self, key):
        h = hash(key) % self.__size
        return self.__obj[h][1]

    def delete(self, key):
        pass
