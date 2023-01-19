class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak_idx = arr.index(max(arr))
        if len(arr) < 3 or arr.count(max(arr)) > 1 or peak_idx in [0, len(arr) - 1]:
            return False
        left = 0
        while left < peak_idx:
            if arr[left] >= arr[left+1]:
                return False
            left += 1
            
        right = peak_idx+1
        while right < len(arr):
            if arr[right-1] <= arr[right]:
                return False
            right += 1
            
        return True
            
        