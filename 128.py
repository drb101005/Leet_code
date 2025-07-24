class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums = list(set(nums))  # remove duplicates
        nums.sort()

        i = 1
        j = 0
        count = 1
        max_count = 1

        while i < len(nums):
            if nums[i] == nums[j] + 1:
                count = count + 1
            else:
                count = 1 
            max_count = max(max_count, count)
            i = i + 1
            j = j + 1

        return max_count
