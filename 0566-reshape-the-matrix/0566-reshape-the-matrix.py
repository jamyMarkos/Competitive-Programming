class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        list_ = [[0] * c for _ in range(r)]
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
            count = 0
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    row = count // c
                    col = count % c
                    list_[row][col] = mat[i][j]
                    count += 1
                    
        return list_
                    
                    
                        

            
        