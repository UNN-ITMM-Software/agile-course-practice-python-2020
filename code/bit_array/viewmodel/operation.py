from enum import Enum


class Operation(Enum):
    NONE = 0
    OR = 1
    AND = 2
    XOR = 3
    EQ = 4
    NEQ = 5
    INVERT = 6
