class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if not grid[i][j]:
                    grid[i][j] = -1

        rowSum = [sum(row) for row in grid]
        colSum = [sum(col) for col in chain(zip(*grid))]

        res = [[0 for j in range(col)] for i in range(row)]
        
        for i in range(row):
            for j in range(col):
                res[i][j] = (rowSum[i] + colSum[j])

        return res