class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(row+1, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        # for row in matrix:
        #     left, right = 0, len(row) - 1
        #     while left < right:
        #         row[left], row[right] = row[right], row[left]
        #         left, right = left+1, right-1
                
            
        