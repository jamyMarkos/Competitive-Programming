class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m-1
        right = n-1
        setter = len(nums1)-1

        if len(nums1) == n:
            for i in range(n):
                nums1[i] = nums2[i]

        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[setter] = nums1[left] 
                left-=1
                setter -=1
            elif nums1[left] <= nums2[right]:
                nums1[setter] = nums2[right] 
                right-=1
                setter -=1
        while right >= 0:
            nums1[setter] = nums2[right] 
            right-=1
            setter -=1