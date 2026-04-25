class Solution(object):
    def findErrorNums(self, nums):
        for x in nums:
            if nums.count(x) == 2:   # Duplicate found
                dup = x
                break
        
        n = len(nums)
        for i in range(1, n + 1):
            if i not in nums:        # Missing number
                missing = i
                break
        
        return [dup, missing]

