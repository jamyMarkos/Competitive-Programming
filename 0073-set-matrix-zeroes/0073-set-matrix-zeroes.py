class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N, M = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        
        # find where the 0's are:
        for row in range(N):
            for col in range(M):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        for i in range(N):
            for j in range(M):
                if i in rows or j in cols:
                    matrix[i][j] = 0
                    
                    
                
        