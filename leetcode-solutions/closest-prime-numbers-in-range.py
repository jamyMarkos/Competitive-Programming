class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True for _ in range(right+1)]
        is_prime[0] = is_prime[1] = False

        i = 2

        while i*i <= right:
            if is_prime[i]:
                j = i*i
                while j <= right:
                    is_prime[j] = False
                    j += i
            i += 1

        lst = []
        for i in range(left, right+1):
            if is_prime[i]:
                lst.append(i)
        diff = float('inf')
        flag = -1
        for i in range(len(lst)-1):
            tt = (lst[i+1] - lst[i])
            if tt < diff:
                diff = tt
                flag = lst[i]

        if diff == float('inf'):
            return [-1, -1]
        return [flag, flag+diff]


            

        

        