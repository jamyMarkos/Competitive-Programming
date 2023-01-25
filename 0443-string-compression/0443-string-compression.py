class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
          0   1   2   3   4   5   6
        ["a","a","b","b","c","c","c"]
        '''
        if len(chars) <= 1:
            return len(chars)
        left, right = 0, 1
        flag = 0
        while right < len(chars):
            if chars[right] == chars[left]:
                right += 1
                
            else:
                chars[flag] = chars[left]
                flag += 1
                temp = right - left
                if temp != 1:
                    for val in str(temp):
                        chars[flag] = val
                        flag += 1
                    
                left = right
                right += 1
        else:
            chars[flag] = chars[left]
            flag += 1
            temp = right - left
            if temp != 1:
                for val in str(temp):
                    chars[flag] = val
                    flag += 1

        return flag
                
            
                
                
                
        