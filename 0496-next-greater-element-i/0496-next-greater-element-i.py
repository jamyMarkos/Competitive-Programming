class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monoStack = []
        
        hashTable = dict()
        
        for num in nums2:
            if not monoStack or monoStack[-1] > num:
                monoStack.append(num)
            else:
                '''
                [1,2,3,4]
                '''
                while monoStack and monoStack[-1] < num:
                    hashTable[monoStack.pop()] = num
                monoStack.append(num)
                    
        print(hashTable)
                    
        res = []
        for num in nums1:
            if num in hashTable:
                res.append(hashTable[num])
            else:
                res.append(-1)
            
        return res
        
                
        