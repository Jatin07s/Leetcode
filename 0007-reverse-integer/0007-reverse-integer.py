class Solution(object):
    def reverse(self, x):
        a = list(str(x))
        b = ''
        for i in range(len(a)-1 , -1 , -1):
            b += a[i]
        if b[-1] == '-':
            b = '-' + b[:-1]
        ans = int(b)

        if ans < -2**31 or ans > 2**31-1:
            return 0
        return ans 