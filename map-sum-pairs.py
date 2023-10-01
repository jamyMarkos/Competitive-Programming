class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.num = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.Hash = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.num += (val - self.Hash[key])

        self.Hash[key] = val


    def sum(self, prefix: str) -> int:
        cur = self.root
        for ch in prefix:
            cur = cur.children[ch]
        return cur.num
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)