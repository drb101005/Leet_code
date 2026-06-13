# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.


# Example 1:

# Input: s = "egg", t = "add"
# Output: true


# Example 2:

# Input: s = "foo", t = "bar"
# Output: false


# Example 3:

# Input: s = "paper", t = "title"
# Output: true


# Constraints:

# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ASCII character.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_st = {}
        map_ts = {}

        for a, b in zip(s, t):
            if a in map_st and map_st[a] != b:
                return False
            if b in map_ts and map_ts[b] != a:
                return False
            map_st[a] = b
            map_ts[b] = a

        return True
