import copy

class Solution:
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()

        def func(li, idx):
            if idx == len(nums):
                result.append(li)
            else:
                func(copy.deepcopy(li), idx + 1)
                func(copy.deepcopy(li) + [nums[idx]], idx + 1)

        func([], 0)
        result = list(set([tuple(item) for item in result]))
        return result