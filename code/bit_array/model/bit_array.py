import copy


class BitArray:
    """
    BitArray is an array data structure that compactly stores bits. The bit storage unit is an 8-bit word.
    """

    def __init__(self, count=None):
        self.__WORD_SIZE = 8

        if count is None:
            raise ValueError('You have to set the number of bit in the array')
        if not isinstance(count, int):
            raise TypeError('The input argument must be a positive integer')
        if count <= 0:
            raise ValueError('The input argument must be positive')

        self.__mem_length = count // self.__WORD_SIZE + 1
        if not count % self.__WORD_SIZE:
            self.__mem_length -= 1

        self.__length = count
        self.__array = [0] * self.__mem_length

    def __or__(self, bit_array):
        if not isinstance(bit_array, BitArray):
            raise TypeError('The input argument must be an instance of BitArray class')

        if self.__length >= bit_array.__length:
            result = copy.deepcopy(self)
        else:
            result = copy.deepcopy(bit_array)

        length = min(self.__mem_length, bit_array.__mem_length)

        for i in range(length):
            result.__array[i] = self.__array[i] | bit_array.__array[i]

        return result

    def __ror__(self, bit_array):
        return self.__or__(bit_array)

    def __and__(self, bit_array):
        if not isinstance(bit_array, BitArray):
            raise TypeError('The input argument must be an instance of BitArray class')

        if self.__length >= bit_array.__length:
            result = BitArray(self.__length)
        else:
            result = BitArray(bit_array.__length)

        length = min(self.__mem_length, bit_array.__mem_length)

        for i in range(length):
            result.__array[i] = self.__array[i] & bit_array.__array[i]

        return result

    def __rand__(self, bit_array):
        return self.__and__(bit_array)

    def __xor__(self, bit_array):
        if not isinstance(bit_array, BitArray):
            raise TypeError('The input argument must be an instance of BitArray class')

        if self.__length >= bit_array.__length:
            result = copy.deepcopy(self)
        else:
            result = copy.deepcopy(bit_array)

        length = min(self.__mem_length, bit_array.__mem_length)

        for i in range(length):
            result.__array[i] = self.__array[i] ^ bit_array.__array[i]

        return result

    def __rxor__(self, bit_array):
        return self.__xor__(bit_array)

    def __invert__(self):
        result = BitArray(self.__length)

        for i in range(self.__mem_length):
            string = self.__decimal_to_binary(self.__array[i])
            element = ''.join('1' if x == '0' else '0' for x in string)
            result.__array[i] = int(element, 2)

        return result

    def __eq__(self, bit_array):
        if not isinstance(bit_array, BitArray):
            raise TypeError('The input argument must be an instance of BitArray class')

        return self.__array == bit_array.__array

    def __ne__(self, bit_array):
        if not isinstance(bit_array, BitArray):
            raise TypeError('The input argument must be an instance of BitArray class')

        return not (self == bit_array)

    def set_bit(self, bit):
        if not isinstance(bit, int):
            raise TypeError('The input argument must be a non-negative integer')
        if bit < 0 or bit >= self.__length:
            raise IndexError('Bit is out of array range')

        self.__array[self.__get_array_index(bit)] |= self.__get_mask(bit)

    def get_bit(self, bit):
        if not isinstance(bit, int):
            raise TypeError('The input argument must be a non-negative integer')
        if bit < 0 or bit >= self.__length:
            raise IndexError('Bit is out of array range')

        return 1 if self.__array[self.__get_array_index(bit)] & self.__get_mask(bit) else 0

    def clear_bit(self, bit):
        if not isinstance(bit, int):
            raise TypeError('The input argument must be a non-negative integer')
        if bit < 0 or bit >= self.__length:
            raise IndexError('Bit is out of array range')

        self.__array[self.__get_array_index(bit)] &= ~self.__get_mask(bit)

    def get_length(self):
        return self.__length

    def get_mem_length(self):
        return self.__mem_length

    def to_string(self):
        string = ''

        for i in range(self.__mem_length):
            string = self.__decimal_to_binary(self.__array[i]) + string

        return string

    def __get_mask(self, bit):
        if not isinstance(bit, int):
            raise TypeError('The input argument must be a non-negative integer')
        if bit < 0 or bit >= self.__length:
            raise ValueError('Bit is out of array range')

        return 1 << (bit % self.__WORD_SIZE)

    def __get_array_index(self, bit):
        if not isinstance(bit, int):
            raise TypeError('The input argument must be a non-negative integer')
        if bit < 0 or bit >= self.__length:
            raise IndexError('Bit is out of array range')

        return bit // self.__WORD_SIZE

    def __decimal_to_binary(self, n):
        if n < 0:
            raise ValueError('The input argument must be a non-negative integer')

        byte_string = bin(n).replace("0b", "")
        byte_string = '0' * (self.__WORD_SIZE - len(byte_string)) + byte_string

        return byte_string
