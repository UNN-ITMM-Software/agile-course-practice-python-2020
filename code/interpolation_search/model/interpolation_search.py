
class InterpolationSearch():
    def __init__(self):
        self.search = list()

    def interpolation_search(self, lst, val):
        low = 0
        high = (len(lst) - 1)
        while low <= high and val >= lst[low] and val <= lst[high]:
            index = low + int(((float(high - low) / (lst[high] - lst[low])) * (val - lst[low])))
            if lst[index] == val:
                return index
            elif lst[index] < val:
                low = index + 1
            else:
                high = index - 1
        return -1
