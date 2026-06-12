# You are given two strings s and t consisting of only lowercase English letters.
# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.


# Example 1:

# Input: s = "coaching", t = "coding"
# Output: 4


# Example 2:

# Input: s = "abcde", t = "a"
# Output: 0


# Example 3:

# Input: s = "z", t = "abcde"
# Output: 5


# Constraints:

# 1 <= s.length, t.length <= 10^5
# s and t consist only of lowercase English letters.


class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j
