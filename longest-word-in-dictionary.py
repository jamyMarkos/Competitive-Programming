# class TrieNode:
#     def __init__(self):
#         self.children = [None for _ in range(26)]
#         self.freq = 0
    

class Solution:

    # def __init__(self):
    #     self.root = TrieNode()
        

    # def insert(self, word: string) -> None:
    #     cur = self.root
    #     for char in word:
    #         idx = ord(char) - ord('a')
    #         if not cur.children[idx]:
    #             cur.children[idx] = TrieNode()
    #         cur.freq += 1
    #         cur = cur.children[idx]

    # def find_longest_word(self) -> str:
    #     longest = []
    #     for idx, cur in enumerate(cur.children):
    #         if not cur: continue
    #         # if cur.freq == cur.children[idx].freq+1:
    #         #     longest.append(idx)
    #         # cur = cur.children[idx]



        


        


    def longestWord(self, words: List[str]) -> str:
        # sorted_list = sorted(words)
        # for word in words:
        #     self.insert(word)


        # return self.find_longest_word()
        words.sort()
        hash_set = set()
        res = ''
        for word in words:
            if len(word) == 1 or word[:-1] in hash_set:
                if len(word) > len(res):
                    res = word
                hash_set.add(word)
                
        return res