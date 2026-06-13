# You have a long flowerbed in which some of the plots are planted and some are not.
# Flowers cannot be planted in adjacent plots.
# Return true if n new flowers can be planted in the flowerbed without violating the rule.


# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true


# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false


# Constraints:

# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
            i += 1
        return n == 0
