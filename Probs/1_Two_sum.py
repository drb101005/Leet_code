# Given an array of integers nums and an integer target, return the indices of the two numbers
# such that they add up to target.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]


# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
