class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # arr = [[1]*n for _ in range(m)]

        # inbound = lambda x, y: x in range(m) and y in range(n)

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if inbound(i, j+1) and inbound(i+1, j):
        #             arr[i][j] = arr[i][j+1] + arr[i+1][j]
              
        # return arr[0][0]
        
        memo = {}
        def dfs(x, y):
            if x == m-1 and y == n-1:
                return 1
            if (x, y) in memo:
                return memo[(x, y)]
            
            if x >= m or y >= n:
                return 0
            
            memo[(x, y)] = dfs(x+1, y) + dfs(x, y+1)
            return memo[(x, y)]

        return dfs(0, 0)