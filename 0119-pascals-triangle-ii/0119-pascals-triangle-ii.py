class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        row = [1]
        triangle = self.getRow(rowIndex - 1)
        
        for i in range(len(triangle) - 1):
            row.append(triangle[i] + triangle[i+1])
            
        row.append(1)
        
        return row
        