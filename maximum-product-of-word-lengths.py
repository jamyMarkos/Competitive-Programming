class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bits = []
        n = len(words)
        max_len = 0

        for word in words:
            tt = [0] * 26
            for ch in word:
                tt[ord(ch) - ord('a')] = 1
            tmp = int(''.join(map(str, tt)), 2)
            bits.append(tmp)

        for i in range(n):
            for j in range(i, n):
                if not bits[i] & bits[j]:
                    max_len = max(max_len, len(words[i] * len(words[j])))

        return max_len