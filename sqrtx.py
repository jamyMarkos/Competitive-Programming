class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            mid = (l + r) // 2
            tmp = mid * mid
            if tmp > x:
                r = mid - 1 
            elif tmp < x:
                l = mid + 1
            else:
                return mid
        return r