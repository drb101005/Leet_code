# A distinct string is a string that is present only once in an array.
# Given an array arr and an integer k, return the kth distinct string in arr.
# If there are fewer than k distinct strings, return an empty string "".


# Example 1:

# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"


# Example 2:

# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"


# Example 3:

# Input: arr = ["a","b","a"], k = 3
# Output: ""


# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i].length <= 5
# arr[i] consists of lowercase English letters.
# 1 <= k <= 1000


class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        freq = {}
        for word in arr:
            freq[word] = freq.get(word, 0) + 1

        for word in arr:
            if freq[word] == 1:
                k -= 1
                if k == 0:
                    return word
        return ""
