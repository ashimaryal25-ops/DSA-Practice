class Solution(object):
    def maxProfit(self, prices):
        minSeen = float('inf')

        maxProfit = 0

        for price in prices:


            curProfit = price - minSeen

           
            minSeen = min( minSeen, price)
            maxProfit = max( curProfit, maxProfit)
        
        return maxProfit