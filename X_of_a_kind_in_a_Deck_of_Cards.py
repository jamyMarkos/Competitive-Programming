class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hash_table = {}
        
        for n in deck:
            hash_table[n] = 1 + hash_table.get(n, 0)
            
        arr = list(hash_table.values())
        
        res = arr[0]
        for i in range(1, len(arr)):
            res = math.gcd(res, arr[i])
        
        return all(arr[i] % res == 0  for i in range(len(arr))) and res != 1
        