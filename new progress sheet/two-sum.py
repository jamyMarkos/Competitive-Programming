class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashTable = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in hashTable:
                return [hashTable[complement], idx]
                
            hashTable[num] = idx

        


        