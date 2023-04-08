class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()
        
        def isPrime(x):
            d = 2
            
            while d * d < x:
                if x % d == 0:
                    return False
                d += 1
            return True
                    
        def findPrimeFact(x):
            nonlocal primes
            d = 2
    
            while d * d <= x:
                while x % d == 0:
                    if isPrime(d):
                        primes.add(d)
                    x //= d
                d += 1

            if x > 1:
                primes.add(x)
        
        for n in nums:
            findPrimeFact(n)
        
        return len(primes)
        