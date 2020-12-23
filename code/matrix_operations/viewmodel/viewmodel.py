from matrix_operations.model.matrix_operations import MatrixOperations


class MatrixOperationsViewModel:
    def __init__(self):
        self.matrix1 = MatrixOperations.make_from_list([[0]*3]*3)
        self.matrix2 = MatrixOperations.make_from_list([[0]*3]*3)
        self.rows = 3
        self.answer = ''
        self.operation = '+'

    def get_number_of_rows(self):
        return self.rows

    def get_matrix1_as_list(self):
        return self.matrix1.get_data_lines()

    def get_matrix2_as_list(self):
        return self.matrix2.get_data_lines()

    def update_matrix1_content(self, content):
        self.matrix1 = MatrixOperations.make_from_list(content)

    def update_matrix2_content(self, content):
        self.matrix2 = MatrixOperations.make_from_list(content)

    def calculate_determinant1(self):
        return MatrixOperations.calculate_det(self.matrix1)

    def calculate_determinant2(self):
        return MatrixOperations.calculate_det(self.matrix2)

    def transpose1(self):
        return MatrixOperations.transpose(self.matrix1).get_data_lines()

    def transpose2(self):
        return MatrixOperations.transpose(self.matrix2).get_data_lines()

    def inverse1(self):
        return MatrixOperations.inverse(self.matrix1).get_data_lines()

    def inverse2(self):
        return MatrixOperations.inverse(self.matrix2).get_data_lines()

    def sum(self):
        return MatrixOperations.add_matrix(self.matrix1, self.matrix2).get_data_lines()

    def mul(self):
        return MatrixOperations.multiply_matrix(self.matrix1, self.matrix2).get_data_lines()

    def calculate(self):
        op_dict = {
            'det1': self.calculate_determinant1,
            'det2': self.calculate_determinant2,
            'Transpose1':   self.transpose1,
            'Transpose2':   self.transpose2,
            'inv1': self.inverse1,
            'inv2': self.inverse2,
            '+':    self.sum,
            '*':    self.mul
        }
        self.answer = op_dict[self.operation]()
        self.success = True
        return self.answer

    def set_operation(self, operation):
        self.operation = operation
