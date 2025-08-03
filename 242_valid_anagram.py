# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        s = sorted(s)
        t = sorted(t)
        if(len(s) == len(t)):
            while(i < len(s)):
                if(s[i] == t[i]):
                    i = i + 1 
                else:
                    return False
            return True
        else:
            return False
Best Solution
