class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 1
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return i, j
                j = j + 1
            i = i + 1