# class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         """
#         :type text1: str
#         :type text2: str
#         :rtype: int
#         """
#         i=0
#         j=0
#         ans1 = 0
#         ans2 = 0
#         prev = 0
#         for a in range(len(text1)):
#             if text1[a] == text2[i]:
#                 ans1 += 1
#                 i += 1
#             prev += 1    
#         # print(ans)        
#         for b in range(len(text2)):
#             if text2[b] == text1[j]:
#                 ans2 += 1
#                 j+= 1
#         # print(max(ans1,ans2))  
#         return max(ans1,ans2)      




class Solution(object):
    def longestCommonSubsequence(self, text1, text2):

        m = len(text1)
        n = len(text2)
        dp = [[ -1 for i in range(n)] for j in range(m)]
        def f(i, j):

            if i == m or j == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
                
            if text1[i] == text2[j]:
                return 1 + f(i + 1, j + 1)

            else:
                ans1 = f(i + 1, j)
                ans2 = f(i, j + 1)

                dp[i][j]=max(ans1, ans2)
                return dp[i][j]

        return f(0, 0)
