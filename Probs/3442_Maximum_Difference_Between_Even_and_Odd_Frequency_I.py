# You are given a string s consisting of lowercase English letters.
# Return the maximum difference between the frequency of one character with odd frequency
# and one character with even frequency.


# Example 1:

# Input: s = "aaaaabbc"
# Output: 3


# Example 2:

# Input: s = "abcabcab"
# Output: 1


# Constraints:

# 3 <= s.length <= 100
# s consists only of lowercase English letters.
# s contains at least one character with odd frequency and one character with even frequency.


class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        max_odd = 0
        min_even = float('inf')

        for count in freq:
            if count == 0:
                continue
            if count % 2 == 1:
                if count > max_odd:
                    max_odd = count
            else:
                if count < min_even:
                    min_even = count

        return max_odd - min_even
