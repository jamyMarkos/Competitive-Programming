class Solution:
    def invert(self, arr: List[int], left: int, right: int) -> None:
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        # arr[:3] = arr[:3][::-1]
        right = len(arr) - 1
        while right > 0:
            left = 0
            max_idx = 0
            while left <= right:
                if arr[left] > arr[max_idx]:
                    max_idx = left
                left += 1
            
            if max_idx != right:
                self.invert(arr, 0, max_idx)
                self.invert(arr, 0, right)
                res.append(max_idx+1)
                res.append(right+1)

            right -= 1
        return res
        
        