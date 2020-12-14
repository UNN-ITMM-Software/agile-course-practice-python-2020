from bisymmetric_matrix.model.bisymmetric import BisymmetricMatrix


class BisymmetricMatrixViewModel:
    def __init__(self):
        self.vector = []
        self.vector_list = []
        self.matrix_size = ""
        self.created_random_matrix = ""
        self.created_matrix_from_vector = ""
        self.button_convert_state = 'disabled'
        self.str_random_matrix = ""
        self.str_matrix_from_vector = ""

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_button_enabled(self):
        self.button_convert_state = 'normal'

    def set_button_disabled(self):
        self.button_convert_state = 'disabled'

    def set_created_random_matrix(self, matrix):
        self.created_random_matrix = matrix

    def set_created_matrix_from_vector(self, matrix):
        self.created_matrix_from_vector = matrix

    def get_created_random_matrix(self):
        return self.created_random_matrix

    def get_created_matrix_from_vector(self):
        return self.created_matrix_from_vector

    def set_vector(self, input_vector):
        if input_vector == '':
            self.set_button_disabled()
        else:
            self.vector = input_vector
            self.set_button_enabled()

    def set_matrix_size(self, value):
        self.matrix_size = value
        self.set_button_enabled()

    def create_random_matrix(self):
        if self.button_convert_state == 'normal':
            matrix = BisymmetricMatrix()
            if self.matrix_size == '2x2':
                self.set_created_random_matrix(self.convert_matrix_in_str1(matrix.generate_random_bisym_matrix(2)))
            elif self.matrix_size == '3x3':
                self.set_created_random_matrix(self.convert_matrix_in_str1(matrix.generate_random_bisym_matrix(3)))
            elif self.matrix_size == '4x4':
                self.set_created_random_matrix(self.convert_matrix_in_str1(matrix.generate_random_bisym_matrix(4)))
            elif self.matrix_size == '5x5':
                self.set_created_random_matrix(self.convert_matrix_in_str1(matrix.generate_random_bisym_matrix(5)))
            elif self.matrix_size == '6x6':
                self.set_created_random_matrix(self.convert_matrix_in_str1(matrix.generate_random_bisym_matrix(6)))

    def convert_matrix_in_str1(self, matrix: list):
        for i in range(int(self.matrix_size[0])):
            for j in range(int(self.matrix_size[0])):
                self.str_random_matrix += str(matrix[i][j])
            self.str_random_matrix += '\n'
        return self.str_random_matrix

    def convert_matrix_in_str2(self, matrix: list):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.str_matrix_from_vector += str(matrix[i][j])
            self.str_matrix_from_vector += '\n'
        return self.str_matrix_from_vector

    def create_matrix_from_vector(self):
        if self.button_convert_state == 'normal':
            matrix = BisymmetricMatrix()
            parametr = self.convert_str_vector_to_list(self.vector)
            self.set_created_matrix_from_vector(self.convert_matrix_in_str2(matrix.generate_bisymmetric_matrix_by_vector(parametr)))

    def convert_str_vector_to_list(self, input_str_vector):
        self.vector_list = [int(x) for x in input_str_vector]
        return self.vector_list
