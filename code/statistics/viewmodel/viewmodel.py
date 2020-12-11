from statistics.model.studentmarks import StudentMarks, Register


class StatisticsViewModel:
    def __init__(self):
        self.instr = ''
        self.answer = ''
        self.journal = Register([])
        self.set_btn_disabled()
        self.marks1 = ([])
        self.marks2 = ([])
        self.marks3 = ([])
        self.txt_from_stud1_txt = ''
        self.txt_from_stud2_txt = ''
        self.txt_from_stud3_txt = ''
        self.count_active_student_textboxes = 1

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'

    def validate_text(self):
        journal = Register([])
        if self.count_active_student_textboxes >= 1:
            try:
                self.marks1 = self.parser_marks(self.txt_from_stud1_txt)
                journal.add_new_student(self.marks1)
            except:
                self.set_btn_disabled()
            else:
                self.set_btn_enabled()

        if self.count_active_student_textboxes >= 2:
            try:
                self.marks2 = self.parser_marks(self.txt_from_stud2_txt)
                journal.add_new_student(self.marks2)
            except:
                self.set_btn_disabled()
            else:
                self.set_btn_enabled()

        if self.count_active_student_textboxes >= 3:
            try:
                self.marks3 = self.parser_marks(self.txt_from_stud3_txt)
                journal.add_new_student(self.marks3)
            except:
                self.set_btn_disabled()
            else:
                self.set_btn_enabled()            

    def set_instr(self, stud1_txt, stud2_txt, stud3_txt):
        self.txt_from_stud1_txt = stud1_txt
        self.txt_from_stud2_txt = stud2_txt
        self.txt_from_stud3_txt = stud3_txt
        self.validate_text()

    def get_instr(self):
        return self.instr

    def get_stud1_txt(self):
        return self.txt_from_stud1_txt

    def set_answer(self, answer_str):
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
