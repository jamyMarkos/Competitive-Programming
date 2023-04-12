class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        max_area = 0
        tt = 0
        
        visit = [[False] * col for _ in range(row)]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def inbound(x, y):
            return x in range(row) and y in range(col)
        
        def dfs(r, c):
            nonlocal tt
            visit[r][c] = True
            tt += 1
           
            for dx, dy in directions:
                new_r = r + dx
                new_c = c + dy
                
                if inbound(new_r, new_c) and grid[new_r][new_c] != 0 and not visit[new_r][new_c]:
                    dfs(new_r, new_c)
        
        for i in range(row):
            for j in range(col):
                if not visit[i][j] and grid[i][j] != 0:
                    dfs(i, j)
                max_area = max(max_area, tt)
                tt = 0
                
        return max_area
        