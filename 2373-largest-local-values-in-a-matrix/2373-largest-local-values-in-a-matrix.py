class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        ans = [[[] for i in range(n-2)] for j in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                maximum = 0
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        maximum = max(maximum , grid[r][c])
                ans[i][j] = maximum
        return ans                


