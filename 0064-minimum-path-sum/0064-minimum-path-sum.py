class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]
        def f(i,j):
            if i==m-1 and j==n-1:
                return grid[i][j]
            if i>m-1 or j>n-1:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            down = f(i+1,j)
            right = f(i,j+1)
            dp[i][j] = grid[i][j] + min(down,right)
            return dp[i][j]
        return f(0,0)            