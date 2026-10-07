class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        target = sum(nums)
        if target%2 == 1:
            return False
        k = target//2
        dp = [[-1 for _ in range(k+1)] for _ in range(n)]
        def f(index,k):
            if k == 0:
                return True
            if index == n:
                return False
            if dp[index][k] != -1:
                return dp[index][k]
            not_take = f(index+1,k)
            take = False
            if nums[index] <= k:
                take = f(index+1 , k-nums[index]) 

            dp[index][k] = take or not_take   
            return dp[index][k]
        return f(0,k)     


