from range.model.range import Range
from range.viewmodel.operation import Operation
<<<<<<< HEAD
from range.logger.reallogger import RealLogger


class RangeViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.logger.log('RangeViewModel started')
        self.__value_1 = None
        self.__value_2 = None
        self.__operation = Operation.CONTAINS
        self.__result = None
        self.__value_2_enabled = False

    def set_operation(self, operation):
        self.__operation = operation
        self.logger.log('Set operation %s' % self.__operation)
        self.__value_2_enabled = (operation != Operation.ALL_POINTS) &\
                                 (operation != Operation.END_POINTS)

    def get_operation(self):
        return self.__operation

    def get_value_2_enabled(self):
        return self.__value_2_enabled

    def __set_result(self, value):
        self.__result = value
        self.logger.log('Set result %s' % self.__result)

    def make_operation(self):
        self.logger.log('Make operation started.')
        try:
            if self.__operation == Operation.CONTAINS:
                if isinstance(self.__value_2, int):
                    self.__set_result(self.__value_1.contains_value(self.__value_2))
                elif isinstance(self.__value_2, list):
                    self.__set_result(self.__value_1.contains_set(self.__value_2))
                else:
                    self.__set_result(self.__value_1.contains_range(self.__value_2))
            if self.__operation == Operation.OVERLAP:
                self.__set_result(self.__value_1.overlaps_range(self.__value_2))
            if self.__operation == Operation.EQUALS:
                self.__set_result(self.__value_1.equals(self.__value_2))
            if self.__operation == Operation.ALL_POINTS:
                self.__set_result(self.__value_1.get_all_points())
            if self.__operation == Operation.END_POINTS:
                self.__set_result(self.__value_1.end_points())
        except Exception as exception:
            self.logger.log('Calc exception: %s' % exception)
            raise Exception from exception

        self.logger.log('Make operation ended.')

    def get_value_1_string(self):
        if self.__value_1 is None:
            return ''
        return self.__value_1.to_string()

    def get_value_2_string(self):
        if self.__value_2 is None:
            return ''
        if isinstance(self.__value_2, Range):
            result = self.__value_2.to_string()
        elif isinstance(self.__value_2, list):
            result = ', '.join([str(elem) for elem in self.__value_2])
        else:
            result = str(self.__value_2)

        return result

    def get_result_string(self):
        if self.__result is None:
            return ''
        if isinstance(self.__result, bool):
            return 'Yes' if self.__result else 'No'
        if isinstance(self.__result, list):
            return ' '.join([str(x) for x in self.__result])

    def clear_result(self):
        self.__result = None
        self.logger.log('Result cleared')

    def set_value_1(self, input_range):
        try:
            self.__value_1 = Range(input_range)
            self.logger.log('Set value 1: %s' % input_range)
        except ValueError as exception:
            self.logger.log('Set value 1 exc: %s' % exception)
            raise ValueError from exception

    def set_value_2(self, input_obj):
        result = []

        if input_obj.isdigit():
            self.__value_2 = int(input_obj)

        # check is input_obj potentially range or list, if it have brackets then it is probably range object
        # otherwise it is probably list
        elif not ('(' in input_obj or '[' in input_obj):
            if ',' in input_obj:
                list_obj = [elem.strip() for elem in input_obj.split(',')]
            else:
                list_obj = input_obj.split()

            for i in range(len(list_obj)):
                if not list_obj[i].isdigit():
                    message = 'Wrong type of obj. Expected: integer or set of integers or range object'
                    self.logger.log('Set value 2 exc: %s' % message)
                    raise TypeError(message)
                result.append(int(list_obj[i]))
            self.__value_2 = result
        else:
            try:
                self.__value_2 = Range(input_obj)
            except ValueError as exception:
                self.logger.log('Set value 2 exc: %s' % exception)
                raise ValueError from exception
        self.logger.log('Set value 2: %s' % input_obj)

