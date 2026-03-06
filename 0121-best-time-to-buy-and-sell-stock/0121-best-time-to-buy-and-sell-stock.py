class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minTillNow = prices[0]
        maxProfit = 0

        for p in prices:
            maxProfit =max(p-minTillNow,maxProfit)
            minTillNow = min(minTillNow,p)
        return maxProfit

