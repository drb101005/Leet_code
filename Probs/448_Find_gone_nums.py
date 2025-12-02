# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        sol = []
        i = 0
        expected = 1
        
        while i < len(nums):
            if nums[i] == expected:
                i += 1
                expected += 1
            elif nums[i] > expected:
                sol.append(expected)
                expected += 1
            else:  
                i += 1

        while expected <= len(nums):
            sol.append(expected)
            expected += 1

        return sol

# Shortest Solution

class Solution(object):
    def findDisappearedNumbers(self, nums):
        new = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in new]
        