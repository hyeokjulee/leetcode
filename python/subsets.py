import copy

class Solution:
    def subsets(self, nums):
        result = []

        def func(li, idx):
            if idx == len(nums):
                result.append(li)
            else:
                func(copy.deepcopy(li), idx + 1)
                func(copy.deepcopy(li) + [nums[idx]], idx + 1)

        func([], 0)
        return result