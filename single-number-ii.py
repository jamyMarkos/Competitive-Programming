class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit32 = [0] * 32
        negs = 0

        for n in nums:
            if n < 0:
                negs += 1

            tt = abs(n)
            i = 0
            while tt:
                bit32[i] += tt&1
                tt >>= 1
                i += 1   

        for i in range(32):
            bit32[i] %= 3 

        ans = int(''.join(map(str, bit32[::-1])), 2)

        if not negs % 3:
            return ans
        return -1 * ans