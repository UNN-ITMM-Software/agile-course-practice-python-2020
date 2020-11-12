from math import sqrt
import warnings


class Vector3d:

    def __init__(self, x: float = 1.0, y: float = 1.0, z: float = 1.0):
        self.x = x
        self.y = y
        self.z = z

    def is_equal(self, x: float, y: float, z: float) -> bool:
        return self.x == x and self.y == y and self.z == z

    def calc_norma(self, norma_type='euclid') -> float:
        x = self.x
        y = self.y
        z = self.z
        quad_sum = 0.0
        if norma_type == 'euclid':
            quad_sum = x * x + y * y + z * z
            quad_sum = sqrt(quad_sum)
        else:
            if norma_type == 'manhattan':
                quad_sum = abs(x) + abs(y) + abs(z)
            else:
                if norma_type == 'chebyshev':
                    quad_sum = abs(x)
                    if abs(y) > quad_sum:
                        quad_sum = abs(y)
                    if abs(z) > quad_sum:
                        quad_sum = abs(z)
                else:
                    warnings.warn("Error! Input type doesn't exist.")
        return quad_sum

    def calc_normalization(self) -> list:
        x = self.x
        y = self.y
        z = self.z
        param_normalization = sqrt(x * x + y * y + z * z)
        if param_normalization == 0.0:
            warnings.warn('Error! Division by zero.')
            return [0.0, 0.0, 0.0]
        result = [x / param_normalization, y / param_normalization, z / param_normalization]
        return result

    def scalar_product(self, vec_x: float, vec_y: float, vec_z: float) -> float:
        return self.x * vec_x + self.y * vec_y + self.z * vec_z

    def vector_product(self, vec_x: float, vec_y: float, vec_z: float) -> list:
        res_x = self.y * vec_z - vec_y * self.z
        res_y = self.x * vec_z - vec_x * self.z
        res_z = self.x * vec_y - vec_x * self.y
        result = [res_x, res_y, res_z]
        return result
