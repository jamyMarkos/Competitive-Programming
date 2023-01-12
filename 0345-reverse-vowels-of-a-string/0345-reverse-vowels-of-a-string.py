class Solution:
    def reverseVowels(self, s: str) -> str:
        list_ = [*s]
        left, right = 0, len(s) - 1
        while left < right:
            vowels = 'aeiouAEIOU'
            if list_[left] in vowels and list_[right] in vowels:
                list_[left], list_[right] = list_[right], list_[left]
                left, right = left + 1, right - 1
            elif list_[left] in vowels and list_[right] not in vowels:
                right -= 1
            elif list_[left] not in vowels and list_[right] in vowels:
                left += 1
            else:
                left, right = left + 1, right - 1
        return ''.join(list_)
                
                
            
        