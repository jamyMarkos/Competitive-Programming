class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        flag = 0
        while flag < len(arr):
            if arr[flag] != 0:
                flag += 1
            else:
                arr.insert(flag+1, 0)
                arr.pop()
                flag += 2
            
                
            
            
                