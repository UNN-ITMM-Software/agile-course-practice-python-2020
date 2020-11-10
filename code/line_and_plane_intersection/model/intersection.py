from typing import Tuple


class Point3D:
    __slots__ = ['x', 'y', 'z']
    
    def __init__(self, *obj):
        obj = obj[0] if len(obj) == 1 else obj
        if isinstance(obj, Point3D):
            coordinates = obj.to_tuple()
        elif isinstance(obj, (list, tuple)):
            for item in obj:
                if not isinstance(item, (int, float)):
                    raise TypeError(
                        'Point3D::init - Incorrect elements type. Expected: list[float], tuple[float]')
            coordinates = obj
        else:
            raise TypeError('Point3D::init - Incorrect argument type. Expected: list[float], tuple[float], Point3D')
        self.__make_point(coordinates)

    def to_tuple(self) -> Tuple[float, float, float]:
        return self.x, self.y, self.z

    def __str__(self):
        return 'Point3D [x: {}, y: {}, z: {}]'.format(self.x, self.y, self.z)

    def __make_point(self, xyz: Tuple[float, float, float]) -> None:
        if len(xyz) != 3:
            raise ValueError('Point3D::__make_point - Point must be in 3D space')
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]


class Plane:
    def __init__(self,
                 x: Tuple[float, float, float],
                 y: Tuple[float, float, float],
                 z: Tuple[float, float, float]) -> None:
        if len(x) != 3 or len(y) != 3 or len(z) != 3:
            raise ValueError('Plane must be in 3D space')

        self.x = x
        self.y = y
        self.z = z


class Line:
    pass


class Intersection:
    pass
