class Student(object):
    @staticmethod
    def is_correct(marks):
        for i in marks:
            if not isinstance(i, int):
                raise TypeError
            if i not in [1, 2, 3, 4, 5]:
                raise ValueError
        return True

    def __init__(self, array_of_marks: list):
        if Student.is_correct(array_of_marks):
            self.marks = array_of_marks

    def amount(self):
        return len(self.marks)

    def average(self):
        summary = 0
        count = self.amount()
        for i in self.marks:
            summary += i
        return summary / count


class Register:
    def __init__(self, students: list):
        self.students = students

    def add(self, student):
        if Student.is_correct(student):
            self.students.append(student)

    def losers(self):
        count = 0
        for student in self.students:
            if student.average() < 3:
                count += 1
        return count

    def success(self):
        count = 0
        for student in self.students:
            if student.average() >= 3.5:
                count += 1
        return count

    def excellent(self):
        count = 0
        for student in self.students:
            if student.average() >= 4.5:
                count += 1
        return count
