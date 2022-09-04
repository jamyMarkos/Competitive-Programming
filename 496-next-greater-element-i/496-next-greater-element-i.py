class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        arr = [-1] * l1
        for i in range(l1):
            j = indexOf(nums2, nums1[i])
            while j < len(nums2):
                if nums2[j] > nums1[i]:
                    arr[i] = nums2[j]
                    break
                j += 1
        return arr
                    
            
            
        