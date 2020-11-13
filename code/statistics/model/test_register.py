import unittest

from studentmarks import StudentMarks, Register


class TestAmountOfMarks(unittest.TestCase):
    def test_correct_amount(self):
        result = StudentMarks([2, 3]).amount_of_marks()
        self.assertEqual(result, 2)

    def test_amount_not_negative(self):
        result = StudentMarks([2, 3]).amount_of_marks()
        self.assertGreaterEqual(result, 0)

    def test_amount_not_string(self):
        result = StudentMarks([2, 3]).amount_of_marks()
        self.assertNotIsInstance(result, str)


class TestCorrectInputValue(unittest.TestCase):
    def test_marks_return_error_message_if_list_is_empty(self):
        self.assertRaisesRegex(Warning, 'Enter marks!', StudentMarks.is_correct, [])

    def test_marks_return_error_message_if_arguments_str(self):
        self.assertRaises(TypeError, StudentMarks.is_correct, ['two', 'three', 'four', 'five'])

    def test_marks_return_error_message_if_arguments_negative(self):
        self.assertRaises(ValueError, StudentMarks.is_correct, [-2, 3, -4, 5])

    def test_marks_return_error_message_if_arguments_less_1(self):
        self.assertRaises(ValueError, StudentMarks.is_correct, [3, 1, 0, 5])

    def test_marks_return_error_message_if_arguments_greater_5(self):
        self.assertRaises(ValueError, StudentMarks.is_correct, [4, 3, 7, 5])


class TestAverageMark(unittest.TestCase):
    def test_correct_average_mark(self):
        result = StudentMarks([2, 3]).average_of_marks()
        self.assertEqual(2.5, result)

    def test_average_mark_not_negative(self):
        result = StudentMarks([2, 3]).average_of_marks()
        self.assertGreaterEqual(result, 0)

    def test_average_mark_not_string(self):
        result = StudentMarks([2, 3]).average_of_marks()
        self.assertNotIsInstance(result, str)


class TestAddStudentInRegister(unittest.TestCase):
    def test_add_student(self):
        journal = Register([])
        petrov = ([2, 3, 4, 5])
        journal.add_new_student(petrov)
        self.assertIn(petrov, journal.students)

    def test_add_two_students(self):
        journal = Register([])
        self.assertRaises(TypeError, journal.add_new_student, ([2, 3, 4, 5], [2]))

    def test_return_error_message_if_add_invalid_type_of_marks(self):
        journal = Register([])
        self.assertRaises(TypeError, journal.add_new_student, ['two', 'three'])

    def test_return_error_message_if_add_negative_marks(self):
        journal = Register([])
        self.assertRaises(ValueError, journal.add_new_student, [-2, 3, -4, 5])

    def test_return_error_message_if_add_mark_less_1(self):
        journal = Register([])
        self.assertRaises(ValueError, journal.add_new_student, [3, 1, 0, 5])

    def test_return_error_message_if_add_mark_greater_5(self):
        journal = Register([])
        self.assertRaises(ValueError, journal.add_new_student, [4, 3, 7, 5])


class TestFailingStudents(unittest.TestCase):
    def test_surnames_of_failing_students(self):
        ivanov = StudentMarks([2, 2, 2, 2])
        smirnov = StudentMarks([2, 3, 2, 2, 3])
        sidorov = StudentMarks([4, 5, 4, 5, 5, 5])
        petrov = StudentMarks([2, 3, 2])
        journal = Register([ivanov, smirnov, sidorov, petrov])
        result = journal.surnames_of_losers()
        self.assertEqual([ivanov, smirnov, petrov], result)

    def test_number_of_failing_student(self):
        ivanov = StudentMarks([2, 2, 2, 2])
        smirnov = StudentMarks([2, 3, 2, 2, 3])
        sidorov = StudentMarks([4, 5, 4, 5, 5, 5])
        petrov = StudentMarks([2, 3, 2])
        journal = Register([ivanov, smirnov, sidorov, petrov])
        result = journal.count_of_losers()
        self.assertEqual(3, result)

    def test_number_of_failing_students_among_successful_student(self):
        ivanov = StudentMarks([2, 3, 4, 5])
        smirnov = StudentMarks([4, 3, 4, 4, 5])
        sidorov = StudentMarks([4, 5, 4, 5, 5, 5])
        journal = Register([ivanov, smirnov, sidorov])
        result = journal.count_of_losers()
        self.assertEqual(0, result)

    def test_number_of_failing_students_not_negative(self):
        sidorov = StudentMarks([4, 5, 4, 5, 5, 5])
        journal = Register([sidorov])
        result = journal.count_of_losers()
        self.assertGreaterEqual(result, 0)


class TestSuccessfulStudents(unittest.TestCase):
    def test_surnames_of_successful_students(self):
        ivanov = StudentMarks([5, 5, 4, 5, 5])
        smirnov = StudentMarks([2, 3, 5, 5, 5, 5, 5])
        sidorov = StudentMarks([3, 5, 4, 3, 3, 3])
        petrov = StudentMarks([2, 4])
        journal = Register([ivanov, smirnov, sidorov, petrov])
        result = journal.students_who_successfully_pass()
        self.assertEqual([ivanov, smirnov, sidorov], result)

    def test_number_of_successful_student(self):
        ivanov = StudentMarks([5, 5, 4, 5, 5])
        smirnov = StudentMarks([2, 3])
        sidorov = StudentMarks([4, 5, 4, 5, 5, 5])
        petrov = StudentMarks([2, 4])
        journal = Register([ivanov, smirnov, sidorov, petrov])
        result = journal.count_of_students_who_successfully_pass()
        self.assertEqual(2, result)

    def test_number_of_successful_students_among_failing_student(self):
        ivanov = StudentMarks([2, 3, 2])
        smirnov = StudentMarks([2, 2, 2, 2, 5])
        sidorov = StudentMarks([3, 3, 4, 3])
        journal = Register([ivanov, smirnov, sidorov])
        result = journal.count_of_students_who_successfully_pass()
        self.assertEqual(0, result)

    def test_number_of_success_students_not_negative(self):
        sidorov = StudentMarks([4, 5, 4, 5, 5, 5])
        journal = Register([sidorov])
        result = journal.count_of_students_who_successfully_pass()
        self.assertGreaterEqual(result, 0)


class TestExcellentStudents(unittest.TestCase):
    def test_surnames_of_excellent_students(self):
        ivanov = StudentMarks([5, 5, 4, 5, 5])
        smirnov = StudentMarks([2, 3])
        sidorov = StudentMarks([4, 5, 4, 5, 5, 5])
        petrov = StudentMarks([2, 4])
        journal = Register([ivanov, smirnov, sidorov, petrov])
        result = journal.surnames_of_excellent_students()
        self.assertEqual([ivanov, sidorov], result)

    def test_number_of_excellent_student(self):
        ivanov = StudentMarks([5, 5, 4, 5, 5])
        smirnov = StudentMarks([2, 3])
        sidorov = StudentMarks([4, 5, 4, 5, 5, 5])
        petrov = StudentMarks([2, 4])
        journal = Register([ivanov, smirnov, sidorov, petrov])
        result = journal.count_of_excellent()
        self.assertEqual(2, result)

    def test_number_of_excellent_students_among_failing_student(self):
        ivanov = StudentMarks([2, 3, 2])
        smirnov = StudentMarks([2, 2, 2, 2, 5])
        sidorov = StudentMarks([3, 3, 4, 3])
        journal = Register([ivanov, smirnov, sidorov])
        result = journal.count_of_excellent()
        self.assertEqual(0, result)

    def test_number_of_excellent_students_not_negative(self):
        sidorov = StudentMarks([4, 5, 4, 5, 5, 5])
        journal = Register([sidorov])
        result = journal.count_of_excellent()
        self.assertGreaterEqual(result, 0)
