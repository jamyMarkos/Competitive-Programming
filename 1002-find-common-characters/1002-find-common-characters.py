class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for letter in words[0]:
            min_ = words[0].count(letter)
            for j in range(len(words)):
                min_ = min(words[j].count(letter), min_)
            if letter not in res and min_ > 0:
                for i in range(min_):
                    res.append(letter)
        return res
