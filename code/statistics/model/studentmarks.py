import statistics


class StudentMarks(object):
    @staticmethod
    def is_correct(list_of_marks):
        if not list_of_marks:
            raise Warning("Enter marks!")
        for mark in list_of_marks:
            if not isinstance(mark, int):
                raise TypeError
            if mark not in [1, 2, 3, 4, 5]:
                raise ValueError
        return True

    def __init__(self, array_of_marks: list):
        if StudentMarks.is_correct(array_of_marks):
            self.marks = array_of_marks

    def amount_of_marks(self):
        return len(self.marks)

    def average_of_marks(self):
        return statistics.mean(self.marks)


class Register:
    def __init__(self, students: list):
        self.students = students

    def add_new_student(self, student):
        if StudentMarks.is_correct(student):
            self.students.append(student)

    def surnames_of_losers(self):
        surnames = []
        for student in self.students:
            if student.average_of_marks() < 3:
                surnames.append(student)
        return surnames

    def count_of_losers(self):
        return len(self.surnames_of_losers())

    def surnames_of_excellent_students(self):
        surnames = []
        for student in self.students:
            if student.average_of_marks() >= 4.5:
                surnames.append(student)
        return surnames

    def count_of_excellent(self):
        return len(self.surnames_of_excellent_students())

    def students_who_successfully_pass(self):
        surnames = []
        for student in self.students:
            if student.average_of_marks() >= 3.5:
                surnames.append(student)
        return surnames

    def count_of_students_who_successfully_pass(self):
        return len(self.students_who_successfully_pass())
