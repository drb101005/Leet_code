# Given an integer array nums of length n, return an array ans of length 2n where ans[i] == nums[i]
# and ans[i + n] == nums[i] for 0 <= i < n.


# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]


# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]


# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            ans.append(num)
        return ans
