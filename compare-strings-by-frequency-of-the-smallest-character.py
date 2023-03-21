class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            c = Counter(word)
            return c[min(c)] 

        words = [f(word) for word in words]
        words.sort()
        N = len(words)

        def query(word):
            word = f(word)
            l = 0 
            r = N
            while l < r:
                m = l + (r-l) // 2 
                if words[m] <= word:
                    l = m+1
                else:
                    r = m
            return N - l

        return [query(word) for word in queries]