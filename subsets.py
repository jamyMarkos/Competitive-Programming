class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        for i in range(pow(2, len(nums))):
            tt = []
            count = 0
            tmp = i
            while tmp:
                if tmp&1:
                    tt.append(nums[count])
                tmp >>= 1
                count += 1
            ans.append(tt)
        
        return ans
        