class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        defdict = defaultdict(int)
        res = []
        
        for num in nums:
            if num:
                product *= num
            else:
                defdict[num] += 1
                
        for i in range(len(nums)):
            if nums[i] != 0 and defdict[0] > 0:
                res.append(0)
            elif nums[i] == 0:
                defdict[0] -= 1
                if defdict[0] > 0:
                    res.append(0)
                else:
                    res.append(product)
                defdict[0] += 1
            elif nums[i] != 0 and defdict[0] == 0:
                res.append(product // nums[i])
                
        return res
                