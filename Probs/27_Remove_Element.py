# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
# Return the number of elements in nums which are not equal to val.


# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2


# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5


# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k
