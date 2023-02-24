class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_ = Counter(s1)
        left, right = 0, 0
        tmp = defaultdict(int)
        
        for right in range(len(s2)):
            if s2[right] in hash_:
                tmp[s2[right]] += 1
            
            if len(tmp) == len(hash_):
                if right - left + 1 == len(s1) and tmp == hash_:
                    return True
                else:
                    while right - left + 1 > len(s1):
                        if s2[left] in tmp:
                            tmp[s2[left]] -= 1
                        left += 1
                    if tmp == hash_:
                        return True
        else:
            while right - left + 1 > len(s1):
                if s2[left] in tmp:
                    tmp[s2[left]] -= 1
                left += 1
            if tmp == hash_:
                return True

        return False
                        
                    
          
            
        