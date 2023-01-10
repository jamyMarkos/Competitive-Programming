class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        arr = []
        sum_ = sum([even for even in nums if even % 2 == 0])
        for query in queries:
            temp = nums[query[1]]
            nums[query[1]] = nums[query[1]] + query[0]
            if temp % 2 != 0 and nums[query[1]] % 2 == 0:
                sum_ += nums[query[1]]
            elif temp % 2 == 0 and nums[query[1]] % 2 == 0:
                sum_ += (nums[query[1]] - temp)
            elif temp % 2 == 0 and nums[query[1]] % 2 != 0:
                sum_ -= temp   
            arr.append(sum_)
        return arr
                
            
            
            
            
            
        