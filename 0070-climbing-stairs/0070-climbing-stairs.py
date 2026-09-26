class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """


        # Memoixation method.... 

        # dp = [-1]*(n+1)
        # def f(index):
        #     if index == 1 or index == 0:
        #         return 1
        #     if dp[index] != -1:
        #         return dp[index]
        #     dp[index] = f(index-1) + f(index-2)
        #     return dp[index]
        # return f(n) 






        # Tabulation METHOD

        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]               