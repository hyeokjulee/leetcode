class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length_of_nums = len(nums)
        for i in range(length_of_nums - 1):
            for j in range(i + 1, length_of_nums):
                if nums[i] + nums[j] == target:
                    return [i,j]