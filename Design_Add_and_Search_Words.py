class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isEndOfWord = True
        

    def search(self, word: str) -> bool:

        def dfs(word, node):

            for i in range(len(word)):
                if word[i] == '.':
                    for child in node.children:
                        if dfs(word[i+1:], node.children[child]):
                            return True
                elif word[i] not in node.children:
                    return False
                
                node = node.children[word[i]]
            return node.isEndOfWord

        return dfs(word, self.root)
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)