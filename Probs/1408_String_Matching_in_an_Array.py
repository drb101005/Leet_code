# Given an array of string words, return all strings in words that is a substring of another word.
# You can return the answer in any order.


# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]


# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]


# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []


# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
