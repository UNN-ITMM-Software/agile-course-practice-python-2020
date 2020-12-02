import math


def is_correct_input_type(value):
    return not isinstance(value, bool) and (isinstance(value, float) or isinstance(value, int))


class QuadraticEquation:
    def __init__(self, a=1, b=0, c=0):
        if not is_correct_input_type(a) or not is_correct_input_type(b) or not is_correct_input_type(c):
            raise TypeError("The arguments type must be 'float' or 'int'")
        if a == 0:
            raise ValueError("The equation is not square. The first argument cannot be zero")
        self.answer = None
        self.a = a
        self.b = b
        self.c = c

    def solution(self):
        self.answer = list()
        if self.b == 0:
            if self.a > 0 and self.c > 0 or self.a < 0 and self.c < 0:
                return self.answer

        disc = self.b ** 2 - 4 * self.a * self.c
        if disc < 0:
            return self.answer
        elif disc == 0:
            x = (-self.b / (2 * self.a))
            self.answer.append(x)
        else:
            x1 = (-self.b + math.sqrt(disc)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(disc)) / (2 * self.a)
            self.answer.extend([x1, x2])
            self.answer.sort()
        return self.answer

    def solution_in_string_format(self):
        if not self.answer:
            self.solution()
        if len(self.answer) == 0:
            return 'No solution'
        elif len(self.answer) == 1:
            return 'Answer:\n x = {}'.format(self.answer[0])
        else:
            return 'Answers:\n x1 = {},\n x2 = {}'.format(self.answer[0], self.answer[1])
