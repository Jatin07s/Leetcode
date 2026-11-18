class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        ans = 0
        for i in range(0,n-1):
            if prices[i] > prices[i+1]:
                continue
            elif prices[i] < prices[i+1]:
                ans += (prices[i+1] - prices[i])     
        return ans   