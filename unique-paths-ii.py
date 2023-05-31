class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        arr = [[0]*n for _ in range(m)]
        arr[m-1][n-1] = 1

        inbound = lambda x, y: x in range(m) and y in range(n)

        if obstacleGrid[m-1][n-1] or obstacleGrid[0][0]:
            return 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j]:
                    arr[i][j] = 0
                else:
                    if inbound(i, j+1):
                        arr[i][j] += arr[i][j+1]
                    if inbound(i+1, j):
                        arr[i][j] += arr[i+1][j]

        return arr[0][0]