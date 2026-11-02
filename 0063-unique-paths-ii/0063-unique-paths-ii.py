class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[-1 for i in range(col)] for j in range(row)]
        def f(r,c):
            if r > row-1 or c > col-1:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == row-1 and c == col-1:
                return 1
            if dp[r][c] != -1:
                return dp[r][c]
            right = f(r,c+1)
            down = f(r+1,c)
            dp[r][c] = right+down
            return dp[r][c]
        return f(0,0)                    