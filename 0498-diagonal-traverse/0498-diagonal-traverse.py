class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        i, j = 0, 0
        
        while i < len(mat) and j < len(mat[0]):
            
            while i >= 0 and j < len(mat[0]):
                res.append(mat[i][j])
                i, j = i - 1, j + 1
            
            i += 1
            if j == len(mat[0]):
                j -= 1
                i += 1
    
            while i < len(mat) and j >= 0 and j < len(mat[0]):
                res.append(mat[i][j])
                i, j = i + 1, j - 1

            j += 1
            if i == len(mat):
                j += 1
                i -= 1

        return res
                
                
        