from bisymmetric_matrix.model.bisymmetric import BisymmetricMatrix


class BisymmetricMatrixViewModel:
    def __init__(self):
        self.create_button_enabled = 'disabled'

    def is_create_random_matrix_button_enabled(self):
        return self.create_button_enabled

    def is_create_matrix_from_vector_button_enabled(self):
        return self.create_button_enabled

    def get_vector(self, vector: list):
        if vector == []:
            self.create_button_enabled = 'disabled'
            return
        self.create_button_enabled = 'enabled'
        return self.create_button_enabled
