from statistics.model.studentmarks import StudentMarks, Register

from statistics.logger.reallogger import RealLogger


def parser_marks(string):
    marks_str = string.split()
    marks_int = []
    for mark_str in marks_str:
        marks_int.append(int(mark_str))
    return marks_int


class StatisticsViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.logger.log("Welcome to academic performance calculator!")

        self.button_convert_state = 'disabled'
        self.stud1 = []
        self.stud2 = []
        self.stud3 = []
        self.marks1_txt = ''
        self.marks2_txt = ''
        self.marks3_txt = ''
        self.count_of_losers = 0
        self.count_of_students_who_successfully_pass = 0
        self.count_of_excellent = 0

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'
        self.logger.log('Button state was set to "normal"')

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'
        self.logger.log('Button state was set to "disabled"')

    def validate_text(self):
        try:
            marks1 = parser_marks(self.marks1_txt)
            self.stud1 = StudentMarks(marks1)
            marks2 = parser_marks(self.marks2_txt)
            self.stud2 = StudentMarks(marks2)
            marks3 = parser_marks(self.marks3_txt)
            self.stud3 = StudentMarks(marks3)

            self.set_btn_enabled()
            self.logger.log('Marks was successfully written: %s, %s, %s' % (marks1, marks2, marks3))
        except:
            self.set_btn_disabled()
            self.logger.log('Invalid input!')

    def set_instr(self, marks1_str, marks2_str, marks3_str):
        self.marks1_txt = marks1_str
        self.marks2_txt = marks2_str
        self.marks3_txt = marks3_str
        self.logger.log('Entered marks: %s, %s, %s' % (self.marks1_txt, self.marks2_txt, self.marks3_txt))

    def get_marks1_txt(self):
        return self.marks1_txt

    def get_marks2_txt(self):
        return self.marks2_txt

    def get_marks3_txt(self):
        return self.marks3_txt

    def get_answer_losers(self):
        return self.count_of_losers

    def get_answer_successfully(self):
        return self.count_of_students_who_successfully_pass

    def get_answer_excellent(self):
        return self.count_of_excellent

    def click_button(self):
        self.logger.log('Button clicked')
        if self.button_convert_state != 'disabled':
            journal = Register([self.stud1, self.stud2, self.stud3])
            self.count_of_losers = journal.count_of_losers()
            self.count_of_students_who_successfully_pass = journal.count_of_students_who_successfully_pass()
            self.count_of_excellent = journal.count_of_excellent()
            self.logger.log('Result: %s, %s, %s' % (self.count_of_losers,
                                                    self.count_of_students_who_successfully_pass,
                                                    self.count_of_excellent))
