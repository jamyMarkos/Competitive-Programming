class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            total = 0
            for num in nums:
                total += math.ceil(num / mid)

            if total <= threshold:
                r = mid
            else:
                l = mid + 1
                
                
        return l