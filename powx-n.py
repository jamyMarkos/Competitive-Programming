class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def func(x, n):
            if not n:
                return 1
            if not n % 2:
                left = func(x, n // 2)
                return left * left
            return x * func(x, n - 1)

        return func(x, abs(n)) if n > 0 else 1 / func(x, abs(n))