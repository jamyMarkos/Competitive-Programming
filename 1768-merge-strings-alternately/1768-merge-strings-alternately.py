class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Using two pointers         
        ptr1, ptr2 = 0, 0
        str_ = ''
        while ptr1 < len(word1) and ptr2 < len(word2):
            str_ += (word1[ptr1] + word2[ptr2])
            ptr1, ptr2 = ptr1 + 1, ptr2 + 1
            
        return str_ + word1[ptr1:] + word2[ptr2:]
            
            
            
            
        
        