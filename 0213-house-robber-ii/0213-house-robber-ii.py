class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return nums[0]

        def solve(start,end):
            dp = [-1]*n

            def f(i):
                if i>end:
                    return 0

                if dp[i] != -1:
                    return dp[i]

                dp[i] = max(nums[i]+f(i+2) , f(i+1))

                return dp[i]

            return f(start)

        return max(
            solve(0,n-2) ,
            solve(1,n-1)
        )                    
