class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        N = len(nums)
        for s in range(N):
            g = nums[s]
            if g == k:
                count += 1
            for e in range(s+1, N):
                g = gcd(g, nums[e])

                if g == k:
                    count += 1

        return count