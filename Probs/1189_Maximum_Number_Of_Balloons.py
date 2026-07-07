# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = {}

        for s in text:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1

        b = count.get('b', 0)
        a = count.get('a', 0)
        l = count.get('l', 0) // 2
        o = count.get('o', 0) // 2
        n = count.get('n', 0)

        return min(b, a, l, o, n)