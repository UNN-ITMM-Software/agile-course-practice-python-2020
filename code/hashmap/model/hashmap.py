
class Hashmap(object):

    def __resize(self):
        self.__size *= 2
        self.__length = 0
        temp_obj = self.__obj
        self.__obj = [[] for _ in range(self.__size)]
        for obj_item in temp_obj:
            for item in obj_item:
                self.insert(*item)
        print(self.__obj)

    def __get_hash(self, key):
        return hash(key) % self.__size

    def __init__(self, size=1009):
        self.__length = 0
        self.__size = size
        self.__obj = [[] for _ in range(size)]

    def update(self, key, value):
        self.delete(key)
        self.insert(key, value)

    def insert(self, key, value):
        h = self.__get_hash(key)
        for item in self.__obj[h]:
            if item[0] == key:
                raise KeyError("Object with key {} already in hashmap".format(key))
        self.__obj[h].append((key, value))

        self.__length += 1
        if self.__length > self.__size * 2 / 3:
            self.__resize()

    def get(self, key):
        h = self.__get_hash(key)
        for item in self.__obj[h]:
            if item[0] == key:
                return item[1]
        raise KeyError("No key {} in hashmap".format(key))

    def delete(self, key):
        h = self.__get_hash(key)
        for item in self.__obj[h]:
            if item[0] == key:
                self.__obj[h].remove(item)
                self.__length -= 1
                return
        raise KeyError("No key {} in hashmap".format(key))

    def keys(self):
        keys = []
        for obj_item in self.__obj:
            for item in obj_item:
                keys.append(item[0])
        return keys
