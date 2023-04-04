from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        sorted_list = SortedList()
        ans = []
        
        for idx in range(len(nums))[::-1]:
            ans.append(bisect_left(sorted_list, nums[idx]))
            sorted_list.add(nums[idx])

        return ans[::-1]
        
        
      
        
        
        