class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        adj_list = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)

        visited = [0] * n

        def dfs(city):
            visited[city] = 1

            for neighbour in adj_list[city]:
                if not visited[neighbour]:
                    dfs(neighbour)

        count = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count += 1
                
        return count        


        