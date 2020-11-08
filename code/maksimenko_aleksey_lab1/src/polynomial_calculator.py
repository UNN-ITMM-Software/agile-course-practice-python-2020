from itertools import zip_longest


def check_zero(coeffs):
        if not isinstance(coeffs, (list, tuple)):
            raise TypeError()
        i = 0
        while coeffs[i] == 0:
            if i == len(coeffs) - 1:
                break
            i += 1
        return coeffs[i:]


class Polynomial:
    def __init__(self, params):
        if not isinstance(params, (list, tuple, Polynomial)):
            raise TypeError()
        if isinstance(params, Polynomial):
            self.coeffs = params.coeffs.copy()
        else:
            if len(params) == 0:
                raise AttributeError()
            if not all(isinstance(coef, int) for coef in params):
                raise TypeError()
            params = check_zero(params)
            if isinstance(params, tuple):
                self.coeffs = list(params)
            else:
                self.coeffs = params

    def __str__(self):
        string = ""
        add_str = " + "
        for n in range(len(self.coeffs)):
            n_coeff = str(self.coeffs[n])
            if (n_coeff == "1") and n != len(self.coeffs)-1:
                    n_coeff = ""
            if n < len(self.coeffs) - 2:
                string = string + n_coeff + "x^" + str(len(self.coeffs) - n - 1) + add_str
            elif n < len(self.coeffs) - 1:
                string = string + n_coeff + "x" + add_str
            else:
                string = string + n_coeff
        return string

    def __repr__(self):
        _str = "Polynomial(" + str(self.coeffs) + ")"
        return _str

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            raise TypeError()
        else:
            if other.coeffs != self.coeffs:
                return False
        return True

    def __add__(self, other):
        res = Polynomial(self.coeffs)
        if isinstance(other, int):
            res.coeffs[-1] += other
            return res
        elif isinstance(other, Polynomial):
            c1 = self.coeffs[::-1]
            c2 = other.coeffs[::-1]
            res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
            res = reversed(res)
            res = list(res)
            res = check_zero(res)
            return Polynomial(res)
        else:
            raise TypeError()

    def __radd__(self, other):
        res = Polynomial(self.coeffs)
        if isinstance(other, int):
            res.coeffs[-1] += other
        else:
            raise TypeError()
        res.coeffs = check_zero(res.coeffs)
        return res

    def __sub__(self, other):
        res = Polynomial(self.coeffs)
        if isinstance(other, int):
            res.coeffs[-1] -= other
            return res
        elif isinstance(other, Polynomial):
            c1 = self.coeffs[::-1]
            c2 = other.coeffs[::-1]
            res = [t1-t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
            res = reversed(res)
            res = list(res)
            res = check_zero(res)
            return Polynomial(res)
        else:
            raise TypeError()

    def __rsub__(self, other):
        res = Polynomial(self.coeffs)
        if isinstance(other, int):
            coeff = [(-1)*t for t in res.coeffs]
            res.coeffs = coeff
            res.coeffs[-1] += other
        else:
            raise TypeError()
        res.coeffs = check_zero(res.coeffs)
        return res

    def __mul__(self, val):
        if isinstance(val, int):
            res = [val*t for t in self.coeffs]
        elif isinstance(val, self.__class__):
            _s = self.coeffs
            _v = val.coeffs
            res = [0]*(len(_s)+len(_v)-1)
            for selfpow, selfco in enumerate(_s):
                for valpow, valco in enumerate(_v):
                    res[selfpow+valpow] += selfco*valco
        else:
            raise TypeError()
        res = list(res)
        res = check_zero(res)
        return self.__class__(res)

    def __rmul__(self, val):
        if isinstance(val, int):
            res = [val*t for t in self.coeffs]
        else:
            raise TypeError()
        res = list(res)
        res = check_zero(res)
        return self.__class__(res)
