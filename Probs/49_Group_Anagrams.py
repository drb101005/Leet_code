# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# Example 2:

# Input: strs = [""]
# Output: [[""]]


# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
