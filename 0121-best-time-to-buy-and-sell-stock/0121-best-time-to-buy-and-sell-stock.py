class Solution(object):
    def maxProfit(self, prices):
        #using pointers

        left = 0

        right = 1

        maxProfit = 0
        
        while right < len( prices ): 

            curProfit = prices[right] - prices[left]

            if prices[left] > prices[right]:
                left = right
            
            maxProfit = max( curProfit, maxProfit)

            right += 1


        return maxProfit    



