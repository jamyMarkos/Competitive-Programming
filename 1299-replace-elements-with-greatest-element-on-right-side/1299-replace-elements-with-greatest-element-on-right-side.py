class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_l = arr[-1]
        ptr = len(arr) - 2
        while ptr >= 0:
            temp = arr[ptr]
            arr[ptr] = max_l
            max_l = max(temp, max_l)
            ptr -= 1
        arr[-1] = -1
        return arr
            
        
            
        