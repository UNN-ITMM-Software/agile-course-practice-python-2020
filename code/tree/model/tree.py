class Tree:
    def __init__(self, data):
        if isinstance(data, int):
            self.left = None
            self.right = None
            self.data = data
        else:
            raise TypeError

    def insert(self, data):
        if isinstance(data, int):
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Tree(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Tree(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data
        else:
            raise TypeError

    def find_value(self, value):
        if isinstance(value, int):
            if value < self.data:
                if self.left is None:
                    return "Not Found"
                return self.left.find_value(value)
            elif value > self.data:
                if self.right is None:
                    return "Not Found"
                return self.right.find_value(value)
            else:
                return self.data
        else:
            raise TypeError