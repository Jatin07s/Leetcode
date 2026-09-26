class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # RECURSSIVE APPROACh


        # n = len(nums)

        # def f(i):
        #     if i >= n:
        #         return 0

        #     pick = nums[i] + f(i+2)
        #     not_pick = f(i+1)

        #     return max(pick , not_pick)
        # return f(0)        







        # MEMOIZATION APPROACH...

        # n = len(nums)
        # dp = [-1]*(n+1)
        # def f(i):
        #     if i>= n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     pick = nums[i] + f(i+2)
        #     not_pick = f(i+1)
        #     dp[i] = max(pick , not_pick)
        #     return dp[i]
        # return f(0) 









        # TABULATION [space optimization ]
        n = len(nums)
        if n==1:
            return nums[0]
        prev = max(nums[1] , nums[0])
        prev2 = nums[0]
        for index in range(2,n):
            pick = nums[index] + prev2
            not_pick = prev

            curr = max(pick , not_pick)

            prev2 = prev 
            prev = curr
        return prev    