class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for row in range(n):
            for num in matrix[row]:
                if num < 1 or num > n:
                    return False
                
            if len(set(matrix[row])) < len(matrix[row]):
                return False
        
        for col in range(m):
            tmp = []
            for row in range(n):
                if matrix[row][col] < 1 or matrix[row][col] > n:
                    return False
                tmp.append(matrix[row][col])
            
            if len(set(tmp)) < len(tmp):
                return False
            
        return True