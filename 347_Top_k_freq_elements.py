# 347. Top K Frequent Elements
# Solved
# Medium
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 # Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_num = {}
        for num in nums:
            if num in freq_num:
                freq_num[num]+=1
            else:
                freq_num[num] = 1
        sorted_items = sorted(freq_num.items(),key = lambda x:x[1],reverse = True)
        result=[]
        for i in range(k):
            result.append(sorted_items[i][0])

        return result