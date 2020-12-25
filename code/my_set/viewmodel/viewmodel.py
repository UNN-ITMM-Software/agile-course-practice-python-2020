from my_set.model.my_set import Set


class SetViewModel:
    def __init__(self):
        self.set_A = Set()
        self.set_B = Set()
        self.result = None
        self.error_msg = None

    def add(self, data, name_set):
        try:
            if name_set == 'A':
                processed_data = eval(data)
                self.set_A.add(processed_data)
            else:
                processed_data = eval(data)
                self.set_B.add(processed_data)
        except:
            self.error_msg = "{}". format("Entered value is not correct!!!")

    def delete(self, data, name_set):
        try:
            if name_set == 'A':
                processed_data = eval(data)
                self.set_A.delete(processed_data)
            else:
                processed_data = eval(data)
                self.set_B.delete(processed_data)
        except:
            self.error_msg = "{}". format("Entered value is not correct!!!")

    def intersection(self):
        self.result = self.set_A.intersection(self.set_B)

        return self.set_to_str(self.result)

    def union(self):
        self.set_A.union(self.set_B)

    def difference(self, mode='A\B'):
        if mode == 'A\B':
            self.result = self.set_A.difference(self.set_B)
        else:
            self.result = self.set_B.difference(self.set_A)

        return self.set_to_str(self.result)

    def set_a_to_str(self):
        return self.set_to_str(self.set_A)

    def set_b_to_str(self):
        return self.set_to_str(self.set_B)

    @staticmethod
    def set_to_str(s: Set):
        return str(s.my_set)

    def get_status(self):
        if self.error_msg is None:
            status = "SUCCESS!!!"
        else:
            status = "ERR: {}".format(self.error_msg)
            self.error_msg = None
        return status
