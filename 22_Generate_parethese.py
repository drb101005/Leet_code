# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def backtrack(curr, openN, closeN):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if openN < n:
                backtrack(curr + "(", openN + 1, closeN)
            if closeN < openN:
                backtrack(curr + ")", openN, closeN + 1)

        backtrack("", 0, 0)
        return res
