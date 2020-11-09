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
            curr_val = nums[index]
            curr_pos = index
            while curr_pos > 0 and nums[curr_pos - 1] > curr_val:
                nums[curr_pos] = nums[curr_pos - 1]
                curr_pos = curr_pos - 1
            nums[curr_pos] = curr_val

        return nums
