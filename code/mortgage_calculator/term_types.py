from enum import Enum


class TermType(Enum):

    MONTHLY = 1
    YEARLY = 2

    def __str__(self):
        return "months" if self.value == self.MONTHLY.value else "years"
