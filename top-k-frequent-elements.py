class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashT = Counter(nums)
        nums = list(hashT.keys())
        l, r = 0, len(nums)-1
        
        def partition(s, e):
            pivot = nums[e]
            pIdx = s
            for i in range(s, e):
                if hashT[nums[i]] > hashT[pivot]:
                    nums[i], nums[pIdx] = nums[pIdx], nums[i]
                    pIdx += 1

            nums[pIdx], nums[e] = nums[e], nums[pIdx]
            return pIdx
            

        def quick_sort(l, r):
            if l < r:
                pIdx = partition(l, r)
                quick_sort(l, pIdx-1)
                quick_sort(pIdx+1, r)

        quick_sort(l, r)
        return nums[:k]