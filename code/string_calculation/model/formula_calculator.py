
class Calculator:
    def __init__(self):
        self.brackets = "()"
        self.string_formula = ''
        self.result = ''
        self.OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                          '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
        self.numbers = '1234567890.'

    def set_formula(self, string_formula):
        self.string_formula = str(string_formula)

    def eval(self):
        parsed_values = self.parse(self.string_formula)
        polish = self.shunting_yard(parsed_values)
        self.result = self.calc(polish)
        return self.result

    def parse(self, formula_string):
        number = ''
        for s in formula_string:
            if s in self.numbers:
                number += s
            elif number:
                yield float(number)
                number = ''
            if s in self.OPERATORS or s in self.brackets:
                yield s
        if number:
            yield float(number)

    def shunting_yard(self, parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in self.OPERATORS:
                while stack and stack[-1] != "(" and \
                        self.OPERATORS[token][0] <= self.OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(self, polish):
        stack = []
        for token in polish:
            if token in self.OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(self.OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]
