class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        m = len(s)
        n = len(p)
        
        hashP = Counter(p)
        
        hashS = Counter(s[:n-1])
        
        for i in range(n-1, m):
            startInd = i - (n - 1)
            hashS[s[i]] += 1
            
            if hashP == hashS:
                res.append(startInd)
            
            hashS[s[startInd]] -= 1
            if hashS[s[startInd]] == 0:
                hashS.pop(s[startInd])
        
        return res
        