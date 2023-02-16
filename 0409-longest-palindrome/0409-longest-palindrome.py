class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_ = dict(sorted(Counter(s).items(), key = lambda x: x[1], reverse=True))
        count = 0
        firstOdd = True
        for key in hash_.keys():
            if hash_[key] % 2:
                if firstOdd:
                    count += hash_[key]
                    firstOdd = False
                    continue
                count += (hash_[key] - 1)
            else:
                count += hash_[key]
                
        return count
            
        
        