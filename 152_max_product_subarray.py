# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

class Solution(object):
    def maxProduct(self, nums):
        max_product = nums[0]
        curr_max = 1
        curr_min = 1

        for num in nums:
            if num == 0:
                curr_max = 1
                curr_min = 1
                max_product = max(max_product, 0)
                continue

            temp = curr_max * num
            curr_max = max(num, temp, curr_min * num)
            curr_min = min(num, temp, curr_min * num)

            max_product = max(max_product, curr_max)

        return max_product
