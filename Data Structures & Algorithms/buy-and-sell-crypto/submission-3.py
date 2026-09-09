class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1 

        maxVal = 0

        while right < len(prices):
            if((prices[right] < prices[left])):
                left = right
            else:
                if((prices[right] - prices[left]) > maxVal):
                    maxVal = prices[right] - prices[left]

                right = right + 1 
            
        return maxVal