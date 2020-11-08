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

    def var(self):
        mean = self.mean()
        tmp = [(x - mean)**2 for x in self.values]
        return Statistics._mean(tmp)

    def med(self):
        tmp = sorted(self.values)
        m = len(tmp)//2
        if len(tmp) % 2 == 0:
            res = (tmp[m] + tmp[m-1])/2
        else:
            res = tmp[m]
        return res

    def bmoment(self, k):
        if k <= 0:
            raise ValueError
        tmp = [x**k for x in self.values]
        return Statistics._mean(tmp)
