class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashTable = {}
        for idx, el in enumerate(nums2):
            hashTable[el] = idx
        res = []
        for el in nums1:
            found = False
            start = hashTable[el] + 1
            while start < len(nums2):
                if nums2[start] > el:
                    res.append(nums2[start])
                    found = True
                    break
                start += 1
            if not found:
                res.append(-1)
        return res
        
        