class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freqArr = [0] * 3
        for el in nums:
            freqArr[el] += 1
        k = 0    
        for i in range(3):
            j = 0
            while j < freqArr[i]:
                nums[k] = i
                j += 1
                k += 1
                
        