class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        ans=0    
        min_buy=prices[0]

        for i in range(1,n):
            currentprofit=prices[i]-min_buy
            ans=max(currentprofit,ans)
            min_buy=min(min_buy,prices[i])
        return ans