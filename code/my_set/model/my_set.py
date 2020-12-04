class Set:
    # The class sets (integer set) using lists
    def __init__(self, elements=None):
        self.my_set = list()
        if elements is None:
            pass
        elif isinstance(elements, list):
            self.my_set = elements
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
        elif isinstance(obj, Set):
            return self.my_set == obj.my_set
        elif isinstance(obj, int):
            if (self.get_size() != 1):
                return False
            else:
                return self.my_set[0] == obj
        else:
            raise TypeError('Input error: argument type must be list or int or another set')

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
        if isinstance(obj, (list, Set)):
            for element in obj:
                self.add(element)
        elif isinstance(obj, int):
            self.add(obj)
        else:
            raise TypeError('Input error: argument type must be list or int or another set')
        return self

    def intersection(self, obj):
        if isinstance(obj, Set):
            result = Set()
            for element in self:
                if element in obj:
                    result.add(element)
            return result
        else:
            raise TypeError('Input error: argument type for operations on sets must be only set')

    def difference(self, obj):
        if isinstance(obj, Set):
            result = Set()
            for element in self:
                if element not in obj:
                    result.add(element)
            return result
        else:
            raise TypeError('Input error: argument type for operations on sets must be only set')

    def is_subset(self, obj):
        if isinstance(obj, Set):
            for element in self:
                if element not in obj:
                    return False
            return True
        else:
            raise TypeError('Input error: argument type for operations on sets must be only set')
