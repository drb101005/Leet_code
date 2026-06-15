# You are given a 0-indexed array of strings details. Each element of details provides information
# about a given passenger compressed into a string of length 15.
# Return the number of senior citizens.
# A passenger is a senior citizen if the age in the string is strictly greater than 60.


# Example 1:

# Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# Output: 2


# Example 2:

# Input: details = ["1313579440F2036","2921522980M5644"]
# Output: 0


# Constraints:

# 1 <= details.length <= 100
# details[i].length == 15
# details[i] consists of digits, uppercase English letters, and lowercase English letters.


class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count = 0
        for passenger in details:
            age = int(passenger[11:13])
            if age > 60:
                count += 1
        return count
