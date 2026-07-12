class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def solve(index , total , subset ,  nums):
            if total == target:
                result.append(subset.copy())
                return 
            elif total > target:
                return 

            if index >= len(nums):
                return 

            Sum = total + nums[index]
            subset.append(nums[index])
            solve(index , Sum , subset , nums)

            Sum = total
            subset.pop()
            solve(index+1 , Sum , subset , nums)

        solve(0 , 0 , [] , candidates)
        return result                