class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = []
        for i in range(n+1):
            row = []
            for j in range(amount+1):
                row.append(-1)
            dp.append(row)
        def f(n,target):
            if target==0:
                return 0
            if target<0:
                return float('inf')
            if n<0:
                return float('inf')
            if dp[n][target] != -1:
                return dp[n][target]        
            take = 1+f(n,target-coins[n])
            not_take = f(n-1,target)

            dp[n][target] = min(take,not_take)
            return dp[n][target]
        ans = f(n-1,amount)   

        if ans == float('inf'):
            return -1

        return ans  

