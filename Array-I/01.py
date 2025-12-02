# class Solution(object):
#     def getConcatenation(self, nums):
#         ans = []
#         for i in range(len(nums)):
#             ans.append(nums[i])
#         for i in range(len(nums)):
#             ans.append(nums[i])
#         return ans
class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums