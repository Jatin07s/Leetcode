class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        ans = []
        # for r in range(row):
        #     row_max = float('-inf')
        #     temp = -1
        #     for c in range(col):
        #         if grid[r][c] > row_max:
        #             row_max = grid[r][c]
        #             temp = max(temp,row_max)
        #     # print(ans)
        #     ans.append(temp)

        # # print(ans)
        # return sum(ans) 
        # def s(grid):

        
        for i in range(len(grid)):
            grid[i].sort()
        # print(grid)           
                
       
        for i in range(len(grid[0])-1,-1,-1):
            temp = -1
            for r in range(len(grid)):
                temp = max(temp,grid[r][i])
            ans.append(temp)
        # print(ans)    
        return  sum(ans)

        