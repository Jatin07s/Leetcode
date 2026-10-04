class Solution(object):
    def minRotations(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        curr = 0
        for ch in s:
            digit = int(ch)
            dist = abs(curr-digit)
            ans += min(dist,10-dist)
            curr = digit
        return ans    
