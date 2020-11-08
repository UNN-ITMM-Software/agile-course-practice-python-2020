class Statistics:
    def __init__(self, values=None):
        if isinstance(values, (int, float)):
            self.values = [values]
        elif isinstance(values, (list, tuple)):
            self.values = values
        else:
            raise TypeError

    @staticmethod
    def _mean(x):
        return sum(x)/len(x)

    def mean(self):
        return Statistics._mean(self.values)
