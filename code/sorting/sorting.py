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
        nums = self.convert_to_array_of_int()[:]

        for index in range(1, len(nums)):
            currVal = nums[index]
            currPos = index
            while currPos > 0 and nums[currPos - 1] > currVal:
                nums[currPos] = nums[currPos - 1]
                currPos = currPos - 1
            nums[currPos] = currVal

        return nums
