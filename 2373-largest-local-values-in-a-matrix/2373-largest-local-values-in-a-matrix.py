class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid) - 2, len(grid[0]) - 2
        res = [[0] * rows for _ in range(cols)]
        
        right, down = 0, 0
        count = 0
        while count < (rows * cols):
            max_ = 0
            for row in range(down, down+3):
                for col in range(right, right+3):
                    max_ = max(grid[row][col], max_)
            res[count//cols][count%cols] = max_
            count += 1
            
            if right + 3 < len(grid[0]):
                right += 1
            elif down + 3 < len(grid):
                down += 1
                right = 0
                
        return res
 
                
                    
                    
        
        