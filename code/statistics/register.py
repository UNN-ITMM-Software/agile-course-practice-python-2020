class Register(object):
    @staticmethod
    def is_correct(marks):
        for i in marks:
            if not isinstance(i, int):
                raise TypeError
            if i not in [1, 2, 3, 4, 5]:
                raise ValueError
        return True

    def __init__(self, array_of_marks: list):
        if Register.is_correct(array_of_marks):
            self.marks = array_of_marks

    def amount(self):
        return len(self.marks)

    def average(self):
        sum = 0
        count = self.amount()
        for i in self.marks:
            sum += i
        return sum / count
