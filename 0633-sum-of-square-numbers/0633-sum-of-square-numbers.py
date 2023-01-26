class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            temp = left ** 2 + right ** 2
            if temp > c:
                right -= 1
            elif temp < c:
                left += 1
            else:
                return True
            
        return False
        