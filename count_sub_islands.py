class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col= len(grid1), len(grid1[0])
        count = 0
        visit = [[False] * col for _ in range(row)]
        
        inbound = lambda x, y : 0 <= x < row and 0 <= y < col # lambda func. to check the bound!
        self.flag = True
        
        def dfs(x, y):
            visit[x][y] = True
            if not grid1[x][y]:
                self.flag = False
            
            for dx, dy in directions:
                
                newX, newY = x + dx, y + dy
                
                if inbound(newX, newY) and not visit[newX][newY] and grid2[newX][newY]:
                    dfs(newX, newY)
                
        for i in range(row):
            for j in range(col):
                if not visit[i][j] and grid2[i][j]:
                    tt = dfs(i, j)
                    if self.flag:
                        count += 1
                    self.flag = True
                        
        return count
        
        