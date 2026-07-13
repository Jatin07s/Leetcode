class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(index , total , subset):
            if total == 0:
                result.append(subset.copy())
                return 
            if total <0:
                return 
            if index >= len(candidates):
                return 

            for i in range(index , len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue

                subset.append(candidates[i])
                Sum = total - candidates[i]
                backtrack(i+1 , Sum , subset)
                subset.pop()    
        backtrack(0 , target , [])
        return result