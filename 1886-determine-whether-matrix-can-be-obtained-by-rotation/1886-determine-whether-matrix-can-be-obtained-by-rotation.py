class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        for _ in range(3):
            self.transpose(mat)
            self.flip(mat)
            
            if mat == target: 
                return True
            
        return False
            
            
    def transpose(self, mat):
        rows, cols = len(mat), len(mat[0])
        for row in range(rows):
            for col in range(row+1, cols):
                mat[row][col], mat[col][row] = mat[col][row], mat[row][col]
        
    def flip(self, mat):
        for row in mat:
            left, right = 0, len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
        
        
        