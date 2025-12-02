class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = list(nums)
        nums2.sort()

        n = len(nums2)
        start = nums2[0]
        start2 = nums2[1]

        while True:
            if start2 - 1 == start:
                start = start + 1
                start2 = nums2[nums2.index(start2) + 1] if nums2.index(start2) + 1 < n else n + 1
                if start2 > nums2[-1]:
                    break
            else:
                return start + 1

        if nums2[0] != 0:
            return 0
        else:
            return nums2[-1] + 1
