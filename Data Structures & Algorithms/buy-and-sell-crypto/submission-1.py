class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        buyPrice=prices[0]
        for i in range(1,len(prices)):
            buyPrice=min(buyPrice,prices[i]) 
            maxProfit=max(maxProfit,prices[i]-buyPrice)
        return maxProfit

        