import unittest

from student import Student, Register


class TestAmountOfMarks(unittest.TestCase):
    def test_correct_amount(self):
        result = Student([2, 3]).amount()
        self.assertEqual(result, 2)

    def test_amount_not_negative(self):
        result = Student([2, 3]).amount()
        self.assertGreaterEqual(result, 0)

    def test_amount_not_string(self):
        result = Student([2, 3]).amount()
        self.assertNotIsInstance(result, str)


class TestCorrectInputValue(unittest.TestCase):
    def test_marks_return_error_message_if_arguments_str(self):
        self.assertRaises(TypeError, Student.is_correct, ['two', 'three', 'four', 'five'])

    def test_marks_return_error_message_if_arguments_negative(self):
        self.assertRaises(ValueError, Student.is_correct, [-2, 3, -4, 5])

    def test_marks_return_error_message_if_arguments_less_1(self):
        self.assertRaises(ValueError, Student.is_correct, [3, 1, 0, 5])

    def test_marks_return_error_message_if_arguments_greater_5(self):
        self.assertRaises(ValueError, Student.is_correct, [4, 3, 7, 5])


class TestAverageMark(unittest.TestCase):
    def test_correct_average_mark(self):
        result = Student([2, 3]).average()
        self.assertEqual(2.5, result)

    def test_average_mark_not_negative(self):
        result = Student([2, 3]).average()
        self.assertGreaterEqual(result, 0)

    def test_average_mark_not_string(self):
        result = Student([2, 3]).average()
        self.assertNotIsInstance(result, str)


class TestAddStudentInRegister(unittest.TestCase):
    def test_add_student(self):
        journal = Register([])
        petrov = ([2, 3, 4, 5])
        journal.add(petrov)
        self.assertIn(petrov, journal.students)

    def test_add_two_students(self):
        journal = Register([])
        self.assertRaises(TypeError, journal.add, ([2, 3, 4, 5], [2]))

    def test_return_error_message_if_add_invalid_type_of_marks(self):
        journal = Register([])
        self.assertRaises(TypeError, journal.add, ['two', 'three'])

    def test_return_error_message_if_add_negative_marks(self):
        journal = Register([])
        self.assertRaises(ValueError, journal.add, [-2, 3, -4, 5])

    def test_return_error_message_if_add_mark_less_1(self):
        journal = Register([])
        self.assertRaises(ValueError, journal.add, [3, 1, 0, 5])

    def test_return_error_message_if_add_mark_greater_5(self):
        journal = Register([])
        self.assertRaises(ValueError, journal.add, [4, 3, 7, 5])


class TestNumberOfFailingStudents(unittest.TestCase):
    def test_number_of_failing_student(self):
        ivanov = Student([2, 2, 2, 2])
        smirnov = Student([2, 3, 2, 2, 3])
        sidorov = Student([4, 5, 4, 5, 5, 5])
        petrov = Student([2, 3, 2])
        journal = Register([ivanov, smirnov, sidorov, petrov])
        result = journal.losers()
        self.assertEqual(3, result)

    def test_number_of_failing_students_among_successful_student(self):
        ivanov = Student([2, 3, 4, 5])
        smirnov = Student([4, 3, 4, 4, 5])
        sidorov = Student([4, 5, 4, 5, 5, 5])
        journal = Register([ivanov, smirnov, sidorov])
        result = journal.losers()
        self.assertEqual(0, result)

    def test_number_of_failing_students_not_negative(self):
        sidorov = Student([4, 5, 4, 5, 5, 5])
        journal = Register([sidorov])
        result = journal.losers()
        self.assertGreaterEqual(result, 0)


class TestNumberOfSuccessfulStudents(unittest.TestCase):
    def test_number_of_successful_student(self):
        ivanov = Student([5, 5, 4, 5, 5])
        smirnov = Student([2, 3])
        sidorov = Student([4, 5, 4, 5, 5, 5])
        petrov = Student([2, 4])
        journal = Register([ivanov, smirnov, sidorov, petrov])
        result = journal.success()
        self.assertEqual(2, result)

    def test_number_of_successful_students_among_failing_student(self):
        ivanov = Student([2, 3, 2])
        smirnov = Student([2, 2, 2, 2, 5])
        sidorov = Student([3, 3, 4, 3])
        journal = Register([ivanov, smirnov, sidorov])
        result = journal.success()
        self.assertEqual(0, result)

    def test_number_of_success_students_not_negative(self):
        sidorov = Student([4, 5, 4, 5, 5, 5])
        journal = Register([sidorov])
        result = journal.success()
        self.assertGreaterEqual(result, 0)


class TestNumberOfExcellentStudents(unittest.TestCase):
    def test_number_of_excellent_student(self):
        ivanov = Student([5, 5, 4, 5, 5])
        smirnov = Student([2, 3])
        sidorov = Student([4, 5, 4, 5, 5, 5])
        petrov = Student([2, 4])
        journal = Register([ivanov, smirnov, sidorov, petrov])
        result = journal.excellent()
        self.assertEqual(2, result)

    def test_number_of_excellent_students_among_failing_student(self):
        ivanov = Student([2, 3, 2])
        smirnov = Student([2, 2, 2, 2, 5])
        sidorov = Student([3, 3, 4, 3])
        journal = Register([ivanov, smirnov, sidorov])
        result = journal.excellent()
        self.assertEqual(0, result)

    def test_number_of_excellent_students_not_negative(self):
        sidorov = Student([4, 5, 4, 5, 5, 5])
        journal = Register([sidorov])
        result = journal.excellent()
        self.assertGreaterEqual(result, 0)
