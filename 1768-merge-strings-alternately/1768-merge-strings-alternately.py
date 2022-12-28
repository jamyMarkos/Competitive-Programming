class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str_ = ''
        len_ = max(len(word1), len(word2))
        for i in range(len_):
            if i < len(word1):
                str_ += word1[i]
            if i < len(word2):
                str_ += word2[i]
                
        return str_
            
            
            
        
        