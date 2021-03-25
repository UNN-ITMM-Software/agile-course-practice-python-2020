from vector_3d.model.vector_3d import Vector3d
from vector_3d.infrastructure.real_logger import RealLogger


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class Vector3dViewModel:
    def __init__(self, logger=RealLogger()):
        self.button_norms = 'disabled'
        self.button_products = 'disabled'
        self.norm_vector = None
        self.first_vector = None
        self.second_vector = None
        self.vec0_x = self.vec1_x = self.vec2_x = None
        self.vec0_y = self.vec1_y = self.vec2_y = None
        self.vec0_z = self.vec1_z = self.vec2_z = None
        self.euclid_norm = 0
        self.manhattan_norm = 0
        self.chebyshev_norm = 0
        self.normalized_vector = [0, 0, 0]
        self.dot_product = 0
        self.cross_product = [0, 0, 0]
        self.logger = logger
        self.logger.log('Logging')

    def set_norm_vector(self, x=0, y=0, z=0):
        self.logger.log('Set norm vector: x = {0}, y = {1}, z = {2}'.format(x, y, z))

        self.button_norms = 'disabled'
        self.vec0_x = x
        self.vec0_y = y
        self.vec0_z = z
        if is_float(x) and is_float(y) and is_float(z):
            self.button_norms = 'normal'
            self.norm_vector = Vector3d(float(x), float(y), float(z))

            self.logger.log('Norm vector coordinates: x = {0}, y = {1}, z = {2}'.format(self.norm_vector.x,
                                                                                        self.norm_vector.y,
                                                                                        self.norm_vector.z))

    def set_product_vectors(self, x1=0, x2=0, y1=0, y2=0, z1=0, z2=0):
        self.logger.log('Set product vectors: x1 = {0}, y1 = {1}, z1 = {2},'
                        ' x2 = {3}, y2 = {4}, z2 = {5}'.format(x1, y1, z1, x2, y2, z2))

        self.vec1_x = x1
        self.vec1_y = y1
        self.vec1_z = z1
        self.vec2_x = x2
        self.vec2_y = y2
        self.vec2_z = z2
        self.button_products = 'disabled'
        if is_float(x1) and is_float(y1) and is_float(z1):
            if is_float(x2) and is_float(y2) and is_float(z2):
                self.button_products = 'normal'
                self.first_vector = Vector3d(float(x1), float(y1), float(z1))
                self.second_vector = Vector3d(float(x2), float(y2), float(z2))

                self.logger.log('First product vector: x = {0}, y = {1}, z = {2},'
                                ' Second product vector: x = {0}, y = {1},'
                                ' z = {2},'.format(self.first_vector.x,
                                                   self.first_vector.y,
                                                   self.first_vector.z,
                                                   self.second_vector.x,
                                                   self.second_vector.y,
                                                   self.second_vector.z))

    def calc_norms(self):
        self.euclid_norm = self.norm_vector.calc_norma(norma_type='euclid')
        self.manhattan_norm = self.norm_vector.calc_norma(norma_type='manhattan')
        self.chebyshev_norm = self.norm_vector.calc_norma(norma_type='chebyshev')
        self.normalized_vector = self.norm_vector.calc_normalization()

        self.logger.log('Calculate Euclid norm: {}'.format(self.euclid_norm))
        self.logger.log('Calculate Manhattan norm: {}'.format(self.manhattan_norm))
        self.logger.log('Calculate Chebyshev norm: {}'.format(self.chebyshev_norm))
        self.logger.log('Calculate normalized vector: {}'.format(self.normalized_vector))

    def calc_products(self):
        x = self.second_vector.x
        y = self.second_vector.y
        z = self.second_vector.z
        self.dot_product = self.first_vector.scalar_product(x, y, z)
        self.cross_product = self.first_vector.vector_product(x, y, z)

        self.logger.log('Calculate dot product: {}'.format(self.dot_product))
        self.logger.log('Calculate cross product: {}'.format(self.cross_product))

    def get_norms_button_state(self):
        self.logger.log('Norm button state: {}'.format(self.button_norms))
        return self.button_norms

    def get_products_button_state(self):
        self.logger.log('Product button state: {}'.format(self.button_products))
        return self.button_products

    def get_vec0_x(self):
        self.logger.log('Norm vector coordinate x = {}'.format(self.vec0_x))
        return self.vec0_x

    def get_vec0_y(self):
        self.logger.log('Norm vector coordinate y = {}'.format(self.vec0_y))
        return self.vec0_y

    def get_vec0_z(self):
        self.logger.log('Norm vector coordinate z = {}'.format(self.vec0_z))
        return self.vec0_z

    def get_vec1_x(self):
        self.logger.log('First product vector coordinate x = {}'.format(self.vec1_x))
        return self.vec1_x

    def get_vec1_y(self):
        self.logger.log('First product vector coordinate y = {}'.format(self.vec1_y))
        return self.vec1_y

    def get_vec1_z(self):
        self.logger.log('First product vector coordinate z = {}'.format(self.vec1_z))
        return self.vec1_z

    def get_vec2_x(self):
        self.logger.log('Second product vector coordinate x = {}'.format(self.vec2_x))
        return self.vec2_x

    def get_vec2_y(self):
        self.logger.log('Second product vector coordinate y = {}'.format(self.vec2_y))
        return self.vec2_y

    def get_vec2_z(self):
        self.logger.log('Second product vector coordinate z = {}'.format(self.vec2_z))
        return self.vec2_z

    def get_euclid_norm(self):
        self.logger.log('Euclid norm: {}'.format(self.euclid_norm))
        return self.euclid_norm

    def get_manhattan_norm(self):
        self.logger.log('Manhattan norm: {}'.format(self.manhattan_norm))
        return self.manhattan_norm

    def get_chebyshev_norm(self):
        self.logger.log('Chebyshev norm: {}'.format(self.chebyshev_norm))
        return self.chebyshev_norm

    def get_normalized_vector(self):
        self.logger.log('Normalized vector: {}'.format(self.normalized_vector))
        return self.normalized_vector

    def get_dot_product(self):
        self.logger.log('Dot product: {}'.format(self.dot_product))
        return self.dot_product

    def get_cross_product(self):
        self.logger.log('Cross product: {}'.format(self.cross_product))
        return self.cross_product
