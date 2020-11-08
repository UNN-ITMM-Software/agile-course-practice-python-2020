stringType = type('')


class Sorting:
    def __init__(self, array):
        self.array = array

    def convert_to_array_of_int(self):
        array_of_int = []

        for i in self.array:
            if type(i) == stringType and not i.isalpha():
                array_of_int.append(int(i))
            if type(i) == stringType and not i.isalpha():
                continue
            if type(i) != stringType:
                array_of_int.append(i)

        return array_of_int

    def insertion_sort(self):
        nums = self.array[:]

        for index in range(1, len(nums)):
            currentValue = nums[index]
            currentPosition = index
            while currentPosition > 0 and nums[currentPosition - 1] > currentValue:
                nums[currentPosition] = nums[currentPosition - 1]
                currentPosition = currentPosition - 1
            nums[currentPosition] = currentValue
        return nums

