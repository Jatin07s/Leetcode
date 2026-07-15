class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ['.'*n for _ in range(n)]

        def is_Safe(row,col,board,n):
            dup_row = row
            dup_col = col

            while row>=0 and col>=0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
                row -= 1


            row = dup_row
            col = dup_col

            while col>=0:
                if board[row][col] == 'Q':
                    return False
                col -= 1

            row = dup_row
            col = dup_col

            while row<n and col>=0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
                row += 1

            return True                        




        def solve(col,ans,board,n):
            if col == n:
                ans.append(list(board))
                return 

            for row in range(n):            # when true, means rakh sakte hai queen waha pe
                if is_Safe(row,col,board,n):
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    solve(col+1,ans,board,n)

                    board[row] = board[row][:col] + '.' + board[row][col+1:]    # agr Q nahi rkh skta then pura aise chala jaega ['....']

        solve(0,ans,board,n)
        return ans



