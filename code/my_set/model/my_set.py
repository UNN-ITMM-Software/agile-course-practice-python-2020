class MySet:
    # The class sets (integer set) using lists
    def __init__(self, elements=None):
        self.my_set = list()
        if isinstance(elements, list):
            self.my_set = elements
        elif elements is None:
            pass
        elif isinstance(elements, int):
            self.my_set.append(elements)
        else:
            raise TypeError('Input error: argument type must be list')

    def get_size(self):
        return len(self.my_set)

    def is_empty(self):
        return self.get_size() == 0

    def __contains__(self, element):
        if element in self.my_set:
            return True
        return False

    def __iter__(self):
        for element in self.my_set:
            yield element

    def __eq__(self, obj):
        if isinstance(obj, list):
            return self.my_set == obj
        elif isinstance(obj, MySet):
            return self.my_set == obj.my_set
        elif isinstance(obj, int):
            if (self.get_size() != 1):
                return False
            else:
                return self.my_set[0] == obj
        else:
            raise TypeError('Input error: argument type must be list or int or another set')
        return self

    def add(self, element):
        if element not in self.my_set:
            self.my_set.append(element)

    def delete(self, element):
        if element not in self.my_set:
            raise ValueError('Set doesnt contain this element')
        else:
            position = self.my_set.index(element)
            del self.my_set[position]

    def union(self, obj):
        if isinstance(obj, list):
            for element in obj:
                self.add(element)
        elif isinstance(obj, MySet):
            self.union(obj.my_set)
        elif isinstance(obj, int):
            self.add(obj)
        else:
            raise TypeError('Input error: argument type must be list or int or another set')
        return self

    def intersection(self, obj):
        if isinstance(obj, MySet):
            result = MySet()
            for element in self:
                if element in obj:
                    result.add(element)
            return result
        else:
            raise TypeError('Input error: argument type for operations on sets must be only set')

    def difference(self, obj):
        if isinstance(obj, MySet):
            result = MySet()
            for element in self:
                if element not in obj:
                    result.add(element)
            return result
        else:
            raise TypeError('Input error: argument type for operations on sets must be only set')
