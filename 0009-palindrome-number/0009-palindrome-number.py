class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        end, first = len(num)-1, 0
        while end > first:
            if num[end] == num[first]:
                end -= 1
                first += 1
                continue
            else:
                return False
        if len(num) == 1:
            return True
        return True
        