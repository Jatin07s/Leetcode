class Solution(object):
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])
        ans = 0

        while True:
            rotten = []

            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 2:
                        # Check all 4 adjacent cells
                        for r, c in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                            if 0 <= r < row and 0 <= c < col:
                                if grid[r][c] == 1:
                                    rotten.append((r, c))

            # No fresh orange can rot in this minute
            if len(rotten) == 0:
                break

            # Rot all oranges found in this minute
            for r, c in rotten:
                grid[r][c] = 2

            ans += 1

        # Check if any fresh orange remains
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return ans