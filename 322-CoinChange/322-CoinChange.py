# Last updated: 5/24/2025, 9:29:10 AM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]=min(dp[i],dp[i-coin]+1)
        
        if dp[amount]!=float('inf'):
            return dp[amount]
        else:
            return -1