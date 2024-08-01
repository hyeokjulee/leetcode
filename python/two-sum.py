class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        second = len(nums) - 1

        nums2 = []

        for i in range(len(nums)):
            nums2.append([nums[i], i])

        nums2.sort()

        while nums2[first][0] + nums2[second][0] != target:
            if nums2[first][0] + nums2[second][0] < target:
                first += 1
            else:
                second -= 1
        
        return [nums2[first][1], nums2[second][1]]