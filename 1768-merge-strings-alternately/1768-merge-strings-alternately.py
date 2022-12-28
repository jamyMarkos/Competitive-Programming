class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = deque(word1)
        word2 = deque(word2)
        
        res = ''
        
        while word1 or word2:
            if word1:
                res += word1.popleft()
            if word2:
                res += word2.popleft()
                
        return res
            
            
            
        
        