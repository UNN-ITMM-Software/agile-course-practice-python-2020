from statistics.model.studentmarks import StudentMarks, Register


class StatisticsViewModel:
    def __init__(self):
        self.instr = ''
        self.answer = ''
        self.journal = Register([])
        self.set_btn_disabled()
        self.marks1 = ([])
        self.count_active_student_textboxes = 1

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'

    def validate_text(self):
        try:
            self.marks1 = self.parser_marks(self.instr)
        except:
            self.set_btn_disabled()
        else:
            self.set_btn_enabled()

    def set_instr(self, instr):
        self.instr = instr
        self.validate_text()

    def get_instr(self):
        return self.instr

    def set_answer(self, answer_str):
        #marks_of_student1 = StudentMarks(self.marks1)
        #self.journal.add_new_student(marks_of_student1)
        self.answer = self.journal.count_of_losers()

    def get_answer(self):
        return self.answer

    def click_button(self):
        self.set_answer(self.instr)

    def parser_marks(self, string):
        marks_str = string.split()
        marks_int = []
        for mark_str in marks_str:
            marks_int.append(int(mark_str))
        return marks_int
