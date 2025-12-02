class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if nums[i] != i:
                return i

        return n
