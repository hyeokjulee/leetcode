from itertools import combinations 

class Solution:
    def subsets(self, nums):
        result = []

        for i in range(len(nums) + 1):
            result = result + list(combinations(nums, i))

        return result