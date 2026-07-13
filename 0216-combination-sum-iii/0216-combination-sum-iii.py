class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def solve(index , total , subset):
            if len(subset) == k:
                if total == n:
                    result.append(subset.copy())
                return 


            for i in range(index , 10):

                subset.append(i)
                solve(i+1 , total+i , subset)

                subset.pop()





        solve(1 , 0 , [])
        return result