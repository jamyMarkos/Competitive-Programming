class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.preCount = 0


class Solution:

    def __init__(self):
        self.root = TrieNode()

    def sumPrefixScores(self, words: List[str]) -> List[int]:

        ans = [0] * len(words) 

        def findScore(idx, word):

            cur = self.root

            tt = 0

            for char in word:
                cur = cur.children[char]
                tt += cur.preCount

            ans[idx] = tt
            


        
        def insertWord(word):
            cur = self.root

            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()

                cur = cur.children[char]
                cur.preCount += 1

            self.isEndOfWord = True
        
        for word in words:
            insertWord(word)

        for idx, word in enumerate(words):

            findScore(idx, word)

            # print(ans)
        
        return ans