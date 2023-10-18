class Solution:
    def countVowels(self, word: str) -> int:
        ans, n, cnt = 0, len(word), 0

        for i in range(n):
            if word[i] in 'aeiou':
                l = n - i
                ans += ((i * l) + l)
            
        return ans