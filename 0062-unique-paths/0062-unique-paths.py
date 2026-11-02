class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1 for i in range(n)] for j in range(m)]
        def f(row,col):
            if row == m-1 and col == n-1:
                return 1
            if row > m-1 or col>n-1:
                return 0    
            if dp[row][col] != -1:
                return dp[row][col]
            right = f(row,col+1)
            down = f(row+1,col)
            dp[row][col] = right+down
            return dp[row][col]
        return f(0,0)             
