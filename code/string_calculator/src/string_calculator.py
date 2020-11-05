import regex as re


class StrCalculatorType(object):
    # Data structure for storing the parsed string
    # Abstraction for StrCalculator
    # Let's get rid of a difficult input string,
    # we will keep only the important details.
    def __init__(self, string, delimiters, numstring, numbers):
        self.string = string
        self.delimiters = delimiters
        self.numstring = numstring
        self.numbers = numbers


class StrCalculatorParser(object):
    # string to StrCalculatorType converter
    DEFAULT_DELIMS = ["\n", ","]
    CUSTOM_DELIM_REGEX = "^([^\d])\n"

    def parse(self, string):
        m = self._check_custom_delim(string)
        if m:
            delimiters, numstring = self._handle_custom_delim(string, m)
        else:
            delimiters, numstring = self._handle_default_delim(string)
        numstring = self.align_delimiters(delimiters, numstring)
        integers = self._split_string(numstring)
        return StrCalculatorType(string, delimiters, numstring, integers)

    def _check_custom_delim(self, string):
        return re.match(self.CUSTOM_DELIM_REGEX, string)

    def _handle_custom_delim(self, string, m):
        delimiters = m.captures(1)
        numstring = re.sub(self.CUSTOM_DELIM_REGEX, "", string)
        return (delimiters, numstring)

    def _handle_default_delim(self, string):
        delimiters = self.DEFAULT_DELIMS
        numstring = string
        return (delimiters, numstring)

    def align_delimiters(self, delimiters, numstring):
        for s in delimiters:
            numstring = numstring.replace(s, ",")
        return numstring

    def _split_string(self, numstring):
        return [int(e) for e in numstring.split(',')]


class StrCalculator(object):
    def add(self, string):
        if string == "":
            return 0
        parser = StrCalculatorParser()
        parsedstr = parser.parse(string)
        self._handle_negative_numbers(parsedstr.numbers)
        return sum(parsedstr.numbers)

    def _handle_negative_numbers(self, numbers):
        negs = [e for e in numbers if e < 0]
        if negs:
            msg = "negatives not allowed: " + ', '.join(str(e) for e in negs)
            raise ValueError(msg)
