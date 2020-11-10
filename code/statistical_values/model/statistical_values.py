class StatisticalValues:
    def __init__(self, values=None):
        if isinstance(values, (int, float)):
            self.values = [values]
        elif isinstance(values, (list, tuple)):
            self.values = values
        else:
            raise TypeError('Argument type must be list or tuple')

    @staticmethod
    def _mean(x):
        return sum(x)/len(x)

    def mean(self):
        return StatisticalValues._mean(self.values)

    def variance(self):
        mean = self.mean()
        tmp = [(x - mean)**2 for x in self.values]
        return StatisticalValues._mean(tmp)

    def median(self):
        tmp = sorted(self.values)
        m = len(tmp)//2
        if len(tmp) % 2 == 0:
            res = (tmp[m] + tmp[m-1])/2
        else:
            res = tmp[m]
        return res

    def begining_moment(self, k):
        if k <= 0:
            raise ValueError('k must be > 0')
        tmp = [x**k for x in self.values]
        return StatisticalValues._mean(tmp)

    def central_moment(self, k):
        if k <= 0:
            raise ValueError('k must be > 0')
        mean = self.mean()
        tmp = [(x - mean)**k for x in self.values]
        return StatisticalValues._mean(tmp)
