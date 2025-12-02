
'''
1 2 3
3 2 1
7 8 1


            bank1   bank2   bank3
customer1       1       2       3
customer2       3       2       1
customer3       7       8       1

output: 1+2+3
        3+2+1
        7+8+1
        Customer 3 is the richest

1 5
7 3
3 5


'''

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
#The term amount directly adds the lines in y asix 
        for amount in accounts:
            wealth = sum(amount)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
 