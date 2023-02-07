class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def isMagicSquare(i,j):
            unique = set()
            square = []
            for k in range(i, i+3):
                tmp = []
                for l in range(j, j+3):
                    if grid[k][l] in unique or (grid[k][l] < 1 or grid[k][l] > 9):
                        return False
                    tmp.append(grid[k][l])
                    unique.add(grid[k][l])
                square.append(tmp)
                        
                    
            sum_ = sum(square[0])
            n = len(square)
            m = len(square[0])
            
            # Rows
            for i in range(n):
                if sum_ != sum(square[i]):
                    return False
            # Cols
            for j in range(m):
                temp = 0
                for i in range(n):
                    temp += square[i][j]
                if temp != sum_:
                    return False
                
            # Diagonals
            if (square[0][0] + square[1][1] + square[2][2]) != sum_:
                return False
            if (square[0][2] + square[1][1] + square[2][0]) != sum_:
                return False
    
            return True
          
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagicSquare(i, j):
                    count += 1
                    
        return count
                    
                
                
                        
                        
        