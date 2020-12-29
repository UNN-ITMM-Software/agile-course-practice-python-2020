from my_set.model.my_set import Set
from my_set.logger.reallogger import RealLogger


class SetViewModel:
    def __init__(self, logger=RealLogger()):
        self.set_A = Set()
        self.set_B = Set()
        self.result = None
        self.error_msg = None
        self.logger = logger
        self.logger.log('Welcome!')

    def add(self, data, name_set):
        try:
            if name_set == 'A':
                self.logger.log('Adding {} to set A'.format(data))
                processed_data = eval(data)
                self.set_A.add(processed_data)
                self.logger.log('Resulting set A: {}'.format(self.set_to_str(self.set_A)))
            else:
                self.logger.log('Adding {} to set B'.format(data))
                processed_data = eval(data)
                self.set_B.add(processed_data)
                self.logger.log('Resulting set B: {}'.format(self.set_to_str(self.set_B)))
        except:
            self.error_msg = "{}". format("Entered value is not correct!!!")
            self.logger.log(self.error_msg)

    def delete(self, data, name_set):
        try:
            if name_set == 'A':
                self.logger.log('Deleting {} from set A'.format(data))
                processed_data = eval(data)
                self.set_A.delete(processed_data)
                self.logger.log('Resulting set A: {}'.format(self.set_to_str(self.set_A)))
            else:
                self.logger.log('Deleting {} from set B'.format(data))
                processed_data = eval(data)
                self.set_B.delete(processed_data)
                self.logger.log('Resulting set B: {}'.format(self.set_to_str(self.set_B)))
        except:
            self.error_msg = "{}". format("Entered value is not correct!!!")
            self.logger.log(self.error_msg)

    def intersection(self):
        self.logger.log('Running intersection A with B')
        self.result = self.set_A.intersection(self.set_B)
        result = self.set_to_str(self.result)
        self.logger.log('Result: {}'.format(result))

        return result

    def union(self):
        self.logger.log('Running union A with B')
        self.set_A.union(self.set_B)
        self.logger.log('Resulting set A: {}'.format(self.set_to_str(self.set_A)))

    def difference(self, mode='A\B'):
        if mode == 'A\B':
            self.logger.log('Running difference A\\B')
            self.result = self.set_A.difference(self.set_B)
        else:
            self.logger.log('Running difference B\\A')
            self.result = self.set_B.difference(self.set_A)

        result = self.set_to_str(self.result)
        self.logger.log('Result: {}'.format(result))

        return result

    def set_a_to_str(self):
        value = self.set_to_str(self.set_A)
        self.logger.log('Setting A to {}'.format(value))
        return value

    def set_b_to_str(self):
        value = self.set_to_str(self.set_B)
        self.logger.log('Setting B to {}'.format(value))
        return value

    @staticmethod
    def set_to_str(s: Set):
        return str(s.my_set)

    def get_status(self):
        if self.error_msg is None:
            status = "SUCCESS!!!"
        else:
            status = "ERR: {}".format(self.error_msg)
            self.error_msg = None
        self.logger.log(status)
        return status
