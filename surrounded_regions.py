class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        inbound = lambda x, y: x in range(row) and y in range(col)
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        visit = set()
        tmp = []
        flag = True
        
        def dfs(x, y):
            nonlocal flag
            visit.add((x, y))
            
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                
                if inbound(newX, newY):
                    if board[newX][newY] == 'O' and (newX, newY) not in visit:
                        tmp.append([newX, newY])
                        dfs(newX, newY)
                else:
                    flag = False
          
        
        for i in range(row):
            for j in range(col):
                if (i, j) not in visit and board[i][j] == 'O':
                    tmp.append([i, j])
                    dfs(i, j)
                    
                    if flag:
                        for x, y in tmp:
                            board[x][y] = 'X'
                    flag = True
                    tmp = []
        
        