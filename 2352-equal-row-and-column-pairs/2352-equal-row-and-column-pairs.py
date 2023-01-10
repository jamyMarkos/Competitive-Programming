class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        rows, cols = [], []
        for i in range(len(grid)):
            row = []
            col = []
            for j in range(len(grid)):
                row.append(grid[i][j])
                col.append(grid[j][i])
            rows.append(row)
            cols.append(col)
        for row in rows:
            for col in cols:
                if row == col:
                    count += 1
        return count
        
        