class MySet:
    # The class sets using lists
    def __init__(self, elements=None):
        self.my_set = list()
        if isinstance(elements, list):
            self.my_set = elements
        elif elements is None:
            pass
        else:
            raise TypeError('Input error: argument type must be list')

    def get_size(self):
        return len(self.my_set)

    def isEmpty(self):
        return self.get_size() == 0

    def __contains__(self, element):
        if element in self.my_set:
            return True
        return False

    
