# You are given a string s. The score of a string is defined as the sum of the absolute
# difference between the ASCII values of adjacent characters.
# Return the score of s.


# Example 1:

# Input: s = "hello"
# Output: 13


# Example 2:

# Input: s = "zaz"
# Output: 50


# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.


class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score
