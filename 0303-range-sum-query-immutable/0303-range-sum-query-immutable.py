class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
        print(self.prefix)
        '''
        [0, -2, -2, 1, -4, -2, -3]
        '''

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)