from typing import List


def check_arg(*types):
    def wrapper(f):
        def wrapped_f(self, *args, **kwds):
            for (a, t) in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError('Not valid argument type. Expected {}.'.format(t))
            if len(args[0]) != len(args[1]):
                raise ValueError('Vectors of different lengths obtained. Distance can only be '
                                 'calculated between vectors of equal length.')
            return f(self, *args, **kwds)
        return wrapped_f
    return wrapper


class VectorMetrics(object):
    def __init__(self):
        pass

    @check_arg(List, List)
    def l1(self, vector_a: List, vector_b: List):

        return sum(abs(a - b) for a, b in zip(vector_a, vector_b))

    @check_arg(List, List)
    def l2(self, vector_a: List, vector_b: List):

        return self.__lp(vector_a, vector_b, 2)

    @check_arg(List, List)
    def l3(self, vector_a: List, vector_b: List):

        return self.__lp(vector_a, vector_b, 3)

    @check_arg(List, List)
    def l4(self, vector_a: List, vector_b: List):

        return self.__lp(vector_a, vector_b, 4)

    @check_arg(List, List)
    def linf(self, vector_a: List, vector_b: List):

        return max(abs(a - b) for a, b in zip(vector_a, vector_b))

    @staticmethod
    def __lp(vector_a: List, vector_b: List, p: int):
        if not isinstance(p, int):
            raise TypeError('Not valid argument type. Expected int.')
        if p <= 0:
            raise ValueError('Invalid value of parameter p. Expected p > 0.')

        return sum(abs(a - b)**p for a, b in zip(vector_a, vector_b))**(1 / p)
