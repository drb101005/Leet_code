#In this problem i have to find the sum of a running array for example 
# Array = (1,3,4,2)
#output = (1,4,8,10)

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
