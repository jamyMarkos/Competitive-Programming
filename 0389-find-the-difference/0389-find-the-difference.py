class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_ = Counter(list(t))
        for char in s:
            if char in dict_:
                dict_[char] -= 1
        return "".join([x for x in dict_ if dict_[x] == 1])