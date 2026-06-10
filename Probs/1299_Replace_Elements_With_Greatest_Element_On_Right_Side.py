# Given an array arr, replace every element in that array with the greatest element among
# the elements to its right, and replace the last element with -1.


# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]


# Example 2:

# Input: arr = [400]
# Output: [-1]


# Constraints:

# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            if current > max_right:
                max_right = current
        return arr
