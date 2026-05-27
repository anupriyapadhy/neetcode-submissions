class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfix=float('-inf')
        buyPrice=prices[0]
        for n in prices:
            buyPrice=min(buyPrice,n)
            maxProfix=max(maxProfix,(n-buyPrice))
        return maxProfix

        