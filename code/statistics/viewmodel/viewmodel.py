from statistics.model.studentmarks import StudentMarks, Register


class StatisticsViewModel:
    def __init__(self):
        self.set_btn_disabled()
        self.marks1 = []
        self.marks2 = []
        self.marks3 = []
        self.txt_from_stud1_txt = ''
        self.txt_from_stud2_txt = ''
        self.txt_from_stud3_txt = ''
        self.count_of_losers = 0
        self.count_of_students_who_successfully_pass = 0
        self.count_of_excellent = 0
        self.answer_of_losers = 0
        self.answer_of_students_who_successfully_pass = 0
        self.answer_of_excellent = 0

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'

    def validate_text(self):
        try:
            self.marks1 = self.parser_marks(self.txt_from_stud1_txt)
            stud1 = StudentMarks(self.marks1)
            self.marks2 = self.parser_marks(self.txt_from_stud2_txt)
            stud2 = StudentMarks(self.marks2)
            self.marks3 = self.parser_marks(self.txt_from_stud3_txt)
            stud3 = StudentMarks(self.marks3)
        except:
            self.set_btn_disabled()
        else:
            self.set_btn_enabled()
            journal = Register([stud1, stud2, stud3])
            self.count_of_losers = journal.count_of_losers()
            self.count_of_students_who_successfully_pass = journal.count_of_students_who_successfully_pass()
            self.count_of_excellent = journal.count_of_excellent()

    def set_instr(self, stud1_txt, stud2_txt, stud3_txt):
        self.txt_from_stud1_txt = stud1_txt
        self.txt_from_stud2_txt = stud2_txt
        self.txt_from_stud3_txt = stud3_txt
        self.validate_text()

    def get_stud1_txt(self):
        return self.txt_from_stud1_txt

    def get_stud2_txt(self):
        return self.txt_from_stud2_txt

    def get_stud3_txt(self):
        return self.txt_from_stud3_txt

    def set_answer_losers(self):
        self.answer_of_losers = self.count_of_losers

    def set_answer_successfully(self):
        self.answer_of_students_who_successfully_pass = self.count_of_students_who_successfully_pass

    def set_answer_excellent(self):
        self.answer_of_excellent = self.count_of_excellent

    def get_answer_losers(self):
        return self.answer_of_losers

    def get_answer_successfully(self):
        return self.answer_of_students_who_successfully_pass

    def get_answer_excellent(self):
        return self.answer_of_excellent

    def click_button(self):
        self.set_answer_losers()
        self.set_answer_successfully()
        self.set_answer_excellent()

    def parser_marks(self, string):
        marks_str = string.split()
        marks_int = []
        for mark_str in marks_str:
            marks_int.append(int(mark_str))
        return marks_int
