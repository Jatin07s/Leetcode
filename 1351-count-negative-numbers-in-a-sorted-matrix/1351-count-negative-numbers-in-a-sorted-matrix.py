class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] <0:
                    ans+=1
        return ans            