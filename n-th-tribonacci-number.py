class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache
        def fib(n):
            if 0 < n <= 2:
                return 1
            elif n == 0:
                return 0

            return fib(n-1) + fib(n-2) + fib(n-3) 

        return fib(n)