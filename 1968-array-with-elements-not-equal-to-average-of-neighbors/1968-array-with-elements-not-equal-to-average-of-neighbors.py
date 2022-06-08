class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        temp = len(nums)
        list1 = [] * len(nums)
        while(len(nums) != 0):
            list1.append(nums.pop())
            if len(list1) == temp:
                break
            list1.append(nums.pop(0))
        return list1
            
                
        
        