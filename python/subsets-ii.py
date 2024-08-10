from itertools import combinations 

class Solution:
    def subsetsWithDup(self, nums):
        result = []

        for i in range(len(nums) + 1):
            result = result + list(combinations(sorted(nums), i))

        return list(set([tuple(item) for item in result]))