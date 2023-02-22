class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        '''
        [0, 1, 8, 11, 17, 22, 28]
        '''
        for i in range(1,len(prefix)):
            if prefix[i-1] == (prefix[-1] - prefix[i]):
                return i - 1
            
        return -1
        